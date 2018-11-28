name = 'B'
typ = 'large'
base = name+'-'+typ+'.'
lines = file(base+'in').readlines()

lines = [line.replace('\n','') for line in lines]

T = int(lines[0])

def solve(n):
    n = [int(ch) for ch in n]
    if len(n) == 1: return str(n[0])+'0'
    for i in xrange(len(n)-2, -1, -1):
        if n[i]<n[i+1]: break
    else:
        n.insert(-1,0)
        ret = ''.join(str(ch) for ch in n[::-1])
        ch = 0
        while ret[ch] == '0': ch += 1
        if ch: ret = ret[ch]+'0'*ch+ret[ch+1:]
        while ret[0] == '0':ret = ret[1]+'0'+ret[2:]
        return ret
    sm_pos = i+1
    for j in xrange(i+2,len(n)):
        if n[j] > n[i] and n[j]<n[sm_pos]:
            sm_pos = j
    sm = n.pop(sm_pos)
    to_sort = n[i:]
    n = n[:i]
    to_sort.sort()
    n.append(sm)
    n.extend(to_sort)
    return ''.join(str(ch) for ch in n)

out = file(base+'out','wb')
for case in xrange(1,T+1):
    N = lines[case]
    K = solve(N)
    out.write('Case #%d: %s\n' % (case,K))

out.close()
