

def solve(s):
    s_set = set([x for x in s])
    base = len(s_set)
    if base == 1:
        base = 2

    _map = dict()
    _map[s[0]]=1
    trans = [1]
    t = 0
    for x in s[1:]:
        if x in _map:
            trans.append(_map[x])
        else:
            _map[x]=t
            trans.append(t)
            t=t+1
            if t==1:
                t=2
    trans.reverse()
    ans = 0
    for i in range(len(trans)):
        ans = ans + base**i*trans[i]
    return ans

print(solve('cats'))

fin = open('A-large.in')
fout = open('out.txt', 'w')
N = int(fin.readline())
for i in range(1, N+1):

    ans = solve(fin.readline().rstrip())
    result = 'Case #%d: %d'%(i, ans)
    print(result)
    fout.write(result+'\n')

fin.close()
fout.close()
