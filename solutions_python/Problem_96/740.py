# a a+2  a+2
def s1(n):
    return (n-4) % 3, (n - 4) / 3

def cs1(a):
    return [a,a+2,a+2]

# a a  a+2
def s2(n):
    return (n-2) % 3, (n-2) / 3

def cs2(a):
    return [a,a,a+2]

# a a+1 a+2
def s3(n):
    return (n-3) % 3, (n-3) / 3

def cs3(a):
    return [a,a+1,a+2]

# a a a
def t1(n):
    return n % 3, n/3

def ct1(a):
    return [a,a,a]

# a a a+1
def t2(n):
    return (n-1) % 3, (n-1) / 3

def ct2(a):
    return [a,a,a+1]

# a a+1 a+1
def t3(n):
    return (n-2) % 3, (n-2) / 3

def ct3(a):
    return [a,a+1,a+1]

def solve():
    A = map(int, raw_input().split(' '))
    # number of elements
    n = A[0]
    s = A[1]
    p = A[2]
#    print 'n',n,'s',s,'p',p
    scores = A[3:]
    scores.sort(reverse=True)
    tests = [t1, t2, t3, s1, s2, s3]
    reconstruct = [ct1, ct2, ct3, cs1, cs2, cs3]
    c = 0
    used = 0
    for score in scores:
        for i in range(len(tests)):
            if i >= 3 and used >= s:
                break
            (t, a) = tests[i](score)
            if t == 0 and a >= 0:
                if max(reconstruct[i](a)) >= p:
                    c += 1
#                    print reconstruct[i](a)
                    if i >= 3:
                        used += 1
                    break
    return c


if __name__ == '__main__':
    t = int(raw_input())
    for case in range(1, t+1):
        print("Case #{0}: {1}".format(case, solve()))
