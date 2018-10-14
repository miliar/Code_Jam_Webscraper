import sys

def run(t):
    n = list(str(raw_input()))
    last = '0'
    for i in range(len(n)):
        if i == 0: continue
        if n[i] < n[i - 1]:
            for j in range(len(n) - int(i)):
                n[i + j] = '9'
            n[i - 1] = str(int(n[i - 1]) - 1)
            while i >= 0:
                if i - 2 >= 0 and n[i - 1] < n[i - 2]:
                    n[i - 2] = str(int(n[i - 2]) - 1)
                    n[i - 1] = '9'
                if n[i - 1] == '0' and i > 1:
                    n[i - 1] = '9'
                i -= 1
    print('Case #{}: {}'.format(t, str(int(''.join(n)))))

T = int(raw_input())
for t in xrange(1, T + 1):
    run(t)
