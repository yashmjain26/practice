def lcs(S1, S2):
    m, n = len(S1), len(S2)
    L = [[0] * (n + 1)] * (m + 1)

    for i in range(m + 1):
        for j in range(n + 1):
            L[i][j] = (
                0
                if not (i and j)
                else L[i - 1][j - 1] + 1
                if S1[i - 1] == S2[j - 1]
                else max(L[i - 1][j], L[i][j - 1])
            )
    
    index = L[m][n]
    lcs_algo = [""] * (index + 1)
    i = m
    j = n

    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs_algo)


S1 = "ABCDEFGHIJKLMNOPQ"
S2 = "XSCANOEIMNOPQ"
print(lcs(S1, S2))
