def rotate(x):
    return (x[-1]+x[:-1])

def all_rotate(x):
    x = str(x)
    L = len(x)
    Z = [x]
    for i in range(L):
        Z.append(rotate(Z[-1]))
    return [int(i) for i in list(set(Z))]

def count_valids(n,a,b):
    return sum([1 for m in all_rotate(n) if a<=n<m<=b])

def solve(a,b):
    return sum([count_valids(i,a,b) for i in range(a,b)])

T = int(raw_input())
for i in range(T):
    a,b = raw_input().split(' ')
    a,b = int(a),int(b)
    print "Case #%d: %d" % (i+1, solve(a,b))
