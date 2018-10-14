import sys

t = int(input())
for m in range(1, t + 1):
    n = [int(s) for s in str(input())]
    for i in range(len(n) - 1, 0, - 1):
        if n[i] < n[i-1]:
            for r in range(i, len(n)):
                n[r] = 9
            if n[i-1] != 0:
                n[i-1] -= 1
            else:
                k = 2
                n[i - 1] = 9
                while i - k > 0 and n[i - k] == 0:
                    n[i - k] = 9
                    k += 1

                if i - k == 0 and n[i - k] == 1:
                    n.pop(0)
                else:
                    n[i - k] -= 1

    print("Case #{}: {}".format(m, int(''.join(str(c) for c in n))))
