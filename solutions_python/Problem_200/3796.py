import sys

def maketidy(n):
    n = list(n)
    tidy = False
    while not tidy:
        tidy = True
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                tidy = False
                n[i] = chr(ord(n[i]) - 1)
                for j in range(i+1, len(n)):
                    n[j] = '9'
                break
    n = ''.join(n).replace('0', ' ').strip()
    return n

n = int(sys.stdin.readline())
for case in range(n):
    s = sys.stdin.readline().strip()
    print("Case #{}: {}".format(case+1, maketidy(s)))