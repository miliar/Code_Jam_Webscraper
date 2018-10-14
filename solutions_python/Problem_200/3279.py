
def tidy_check(N):
    for i in range(len(N)-1):
        if N[i+1] < N[i]:
            return i
    return -1
        
def solve(N):
    c = tidy_check(N)
    if c == -1:
        N = filter(lambda a: a != 0, N)
        for i in range(len(N)):
            if N[i] == 10:
                N[i] = 9
        return ''.join(map(str,N))
    else:
        N[c] = N[c] - 1
        N[c+1] = 10
        return solve(N)
        
def dummy_solve(N):
    for i in reversed(xrange(1,N+1)):
        if tidy_check(map(int, str(i))) == -1:
            return str(i)

'''
for i in range(1,1001):
    expected = dummy_solve(i)
    actual = solve(map(int, str(i)))
    if expected != actual:
        print "Failed at expected: " + expected + " actual: " + actual

'''
out = open('tidy_output.txt', 'w')
with open('B-large.in') as f:
    T = int(f.readline().strip())
    for case_num in range(T):
        N = map(int,f.readline().strip())
        ans = solve(N)
        out.write("Case #%d: %s\n"%(case_num+1,ans))
out.close()    
