N = int(input())
dp = [[0]*10 for _ in range(N+1)]

# 1 자리 수는 0을 제외하고 1로 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 뒤에 있는 숫자를 기준으로 앞에 올 수 있는 숫자의 경우의 수
# 2 자리 수부터 시작
for i in range(2, N+1):     # N자리 수
    for j in range(10):     # 0~9
        # 뒤에 있는 수가 0일 때는 앞에 1밖에 오지 못함
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        # 뒤에 있는 수가 9일 때는 앞에 8밖에 오지 못함
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        # 뒤에 있는 수가 2~8일 때는 앞에 숫자가 2개씩 올 수 있음
        # 그 두 숫자로 오기까지의 경우의 수를 합함
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
