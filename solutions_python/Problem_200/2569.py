import sys
sys.stdout = open("out.txt", "w")

def is_tidy(a):
    for i in range(len(a)-1):
        if int(a[i])>int(a[i+1]):
            return False
    return True

def make_tidy(x):
    if is_tidy(x):
        return x
    l = list(x)
    for i in range(len(x)-1):
        if l[i]>l[i+1]:
            l[i] = str(int(l[i])-1)
            for j in range(i+1, len(x)):
                l[j]='9'
            break
    return make_tidy("".join(l))

def solve(x):
    return str(int(make_tidy(x)))
    pass


lines = []

with open("B-large.in", "r") as f:
    lines = f.readlines()

n = int(lines[0])

for i in range(1, n+1):
    ans = solve(lines[i].strip())
    print("Case #{}: {}".format(i, str(ans)))
