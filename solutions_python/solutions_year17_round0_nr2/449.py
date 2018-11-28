def greedy(case):
    n = list(input())
    for i in range(len(n)):
        n[i] = ord(n[i]) - ord("0")
    for i in range(len(n)-1):
        if n[-2-i] > n[-1-i]:
            n[-2-i] -= 1
            for j in range(i+1):
                n[-1-j] = 9
    for i in range(len(n)):
        n[i] = chr(n[i] + ord("0"))
    print("Case #" + str(case) + ": " + str(int("".join(n))))

c = int(input())
for i in range(c):
    greedy(i+1)