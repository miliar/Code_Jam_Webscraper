
def solve(s,k):
    ret = 0
    curr = 0
    while not all(s):
        curr = s.index(False, curr)
        if curr + k > len(s):
            return 'IMPOSSIBLE'
        for i in range(curr, curr + k):
            s[i] = not s[i]
        ret += 1
    return str(ret)
        
    

f = open('in.txt')

cases = int(f.readline())
for i in range(1, cases + 1):
    t = f.readline().split()
    #s = t[0]
    s = [True if v == '+' else False for v in t[0]]
    k = int(t[1])
    print('Case #%s: '%i + solve(s,k))
    
