def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i
            else:
                dp[i][j] = 0

    return s1[end - max_length: end]

s1 = "ABCBDAB"
s2 = "BDCABA"
print(longest_common_substring(s1, s2))  # "BCBA"
