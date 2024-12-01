def gridpaths(M, N, x1, y1, x2, y2):
    dp = [[0 for j in range(N)] for i in range(M)]
    dp[x1][y1] = 1

    for i in range(M):
        for j in range(N):
            if i == x1 and j == y1:
                continue
            if i < x2 or j < y2:
                dp[i][j] = 0
                continue
            if i == x2 and j == y2:
                if (i-1 == x1 and j == y1) or (i == x1 and j-1 == y1):
                    dp[i][j] = 1
                continue

            if i > 0 and dp[i-1][j] > 0 and i-1 >= x2 and (j == y2 or i-1 > x1):
                dp[i][j] += dp[i-1][j]
            if j > 0 and dp[i][j-1] > 0 and j-1 >= y2 and (i == x2 or j-1 > y1):
                dp[i][j] += dp[i][j-1]
            if i < M-1 and dp[i+1][j] > 0 and i+1 <= x2 and (j == y2 or i+1 < x1):
                dp[i][j] += dp[i+1][j]
            if j < N-1 and dp[i][j+1] > 0 and j+1 <= y2 and (i == x2 or j+1 < y1):
                dp[i][j] += dp[i][j+1]

    return dp[x2][y2]
print(gridpaths(9, 6, 2, 2, 6, 4))