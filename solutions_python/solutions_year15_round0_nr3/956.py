import sys

f = sys.stdin #open('C-small-practice.in')
def get_int(): return int(f.readline())
def get_ints(): return [int(s) for s in f.readline().split()]

one = (False, '1')

def mul(x, y):
    res = [False, '']
    if x[1] == '1':
        res[1] = y[1]
    elif y[1] == '1':
        res[1] = x[1]
    elif x[1] == y[1]:
        res = [True, '1']
    else:
        res = [(ord(x[1])-ord(y[1])+3)%3 == 1, (set('ijk') - set((x[1], y[1]))).pop()]
    res[0] = res[0] != (x[0] != y[0])
    return tuple(res)

def eval(s):
    res = one
    for c in s:
        res = mul(res, (False, c))
    return res

def solve(s):
    left = one
    for i in range(len(s)):
        left = mul(left, (False, s[i]))
        if left == (False, 'i'):
            s = s[i+1:]
            break
    else:
        return False
    mid = one
    for i in range(len(s)):
        mid = mul(mid, (False, s[i]))
        if mid == (False, 'j'):
            s = s[i+1:]
            break
    else:
        return False
    return  eval(s) == (False, 'k')

for t in range(get_int()):
    l, x = get_ints()
    s = x * f.readline().strip()
    print("Case #{}: {}".format(t+1, "YES" if eval(s) == (True, '1') and solve(s) else "NO"))
