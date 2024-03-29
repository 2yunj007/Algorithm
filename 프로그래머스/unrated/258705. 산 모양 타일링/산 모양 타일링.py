def solution(n, tops):
    answer = 0
    MOD = 10007
    
    dp = [[0] * 2 for _ in range(n + 1)]
    # dp[i][1]은 i-1번째의 역삼각형이 오른쪽 삼각형과 합친 마름모인 경우 (1)
    # dp[i][0]은 i-1번째의 역삼각형이 오른쪽 삼각형과 합친 마름모가 아닌 경우 (2)
    
    dp[0][0] = 1
    for i in range(n):
        # tops[i]가 1이고 (1)의 경우라면 2가지 경우의 수가 발생하고, (2)의 경우라면 3가지 경우의 수가 발생
        # tops[i]가 0이고 (1)의 경우라면 1가지 경우의 수가 발생하고, (2)의 경우라면 2가지 경우의 수가 발생
        # 경우: 삼각형으로만, 자신과 위쪽 삼각형을 합친 마름모, 자신과 왼쪽 삼각형을 합친 마름모
        dp[i + 1][0] = (dp[i][0] * (2 + tops[i]) + dp[i][1] * (1 + tops[i])) % MOD
        # 현재 삼각형이 오른쪽 삼각형과 합쳐질 때의 경우의 수는 이전 역삼각형이 오른쪽 삼각형과 합쳐진 경우 + 합쳐지지 않은 경우 
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % MOD
        
    answer = (dp[n][0] + dp[n][1]) % MOD
    
    return answer