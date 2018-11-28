def getlist(fr):
    n = int(fr.readline())
    mp = [fr.readline() for i in xrange(4)]
    return map(int, mp[n - 1].split(' '))

def solve(fr):
    la = getlist(fr)
    lb = getlist(fr)
    cnt = 0
    ans = 0
    for a in la:
        if a in lb:
            cnt += 1
            ans = a
    if 0 == cnt:
        return 'Volunteer cheated!'
    elif 1 == cnt:
        return ans
    else:
        return 'Bad magician!'

fr = open('A-small-attempt0.in', 'r')
fw = open('A-small-attempt0.out', 'w')
cas = int(fr.readline())
for ci in xrange(cas):
    fw.write('Case #%d: %s\n' % (ci + 1, solve(fr)))