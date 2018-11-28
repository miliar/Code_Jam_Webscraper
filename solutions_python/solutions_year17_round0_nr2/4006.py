# solves the tidy number problem #

n_cases = int(input())
for i in range(1, n_cases + 1):
    n = str(input())
    for _ in range(len(n)):
        for j in range(len(n) - 1):
            a = int(n[j])
            b = int(n[j + 1])
            if a > b:
                n = n[:j] + str(a - 1) + "9" * (len(str(n)) - j - 1)
    n = int(n)
    print("Case #" + str(i) + ": " + str(n))
