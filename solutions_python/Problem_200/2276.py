T = int(input())
ans = []

def is_tidy(num):
    num = str(num)
    prev = num[0]
    for n in num:
        if n < prev:
            return False
        prev = n
    return True

def descending_idx(num):
    num = str(num)
    prev = num[0]
    i = 0
    for n in num:
        if n < prev:
            return i
        prev = n
        i += 1
    return i

for _ in range(T):
    N = int(input())
    size = len(str(N))
    while N >= 0:
        if is_tidy(N):
            ans.append(N)
            break
        i = descending_idx(N)
        N = int( str(N)[:i+1] + (size - i -1)*'0')
        N -= 1

f = open('output', 'w')
for i, a in enumerate(ans):
    f.write("Case #%i: %s" % ((i+1), str(a)))
    f.write('\n')
f.close
