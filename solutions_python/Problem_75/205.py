'''
Created on 07.05.2011

@author: shelajev
'''
def invoke(q, subs, dels):
    ans = q[0]
    for i in range(1, len(q)):
        cur = q[i]
        while len(ans) > 0 and (ans[-1], cur) in subs:
            cur = subs[(ans[-1], cur)]
            ans = ans[:-1]
        ans += cur
        for c in ans:
            if (cur, c) in dels:
                ans = ''
                break
    return ans        

def solve(params):
    subs = {}
    dels = set()
    n = int(params[0])
    for i in range(n):
        s = params[1+i]
        subs[(s[0], s[1])] = s[2]
        subs[(s[1], s[0])] = s[2]
    offset = n + 1
    m = int(params[offset])
    for i in range(m):
        s = params[i + 1 + offset]
        dels.add((s[0], s[1]))
        dels.add((s[1], s[0]))
    q = params[-1]
    word = invoke(q, subs, dels)
    return '[' + ', '.join(word) + ']'
if __name__ == '__main__':
#    f = open('B-small-attempt0.in', 'r')
#    name = 'B-small-attempt%d' % 0
    name = 'B-large'
    f = open(name + '.in', 'r')
    out = open(name + '.out', 'w')
    T = int(f.readline())
    for t in range(1, T+1):
        ans = solve(f.readline().split())
        print('Case #%s: %s' % (t, ans))
        out.write('Case #%s: %s\n' % (t, ans))
    out.close()