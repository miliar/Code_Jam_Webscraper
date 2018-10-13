r = open('C:/users/hasmeet/desktop/B-large.in', 'r')

w = open('output.txt', 'w')

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


answer = ''

numCases = int(r.readline())

for i in range(numCases):
    print i
    line = r.readline().split(' ')
    N = int(line[0])
    slarbs = []
    for k in range(1,N+1): slarbs.append(int(line[k]))
    answer = 'Case #' + str(i+1) + ': '
    slarbs.sort()
    diffs = []
    for s in range(len(slarbs)):
        for s2 in range(s+1, len(slarbs)): diffs.append(slarbs[s2] - slarbs[s])
    diffs.sort()
    if len(diffs) > 1: gg = gcd(diffs[0], diffs[1])
    else: gg = diffs[0]
    for j in range(2,len(diffs)): gg = gcd(gg, diffs[j])
    if slarbs[0] % gg == 0: answer += '0\n'
    else: answer += str((slarbs[0]/gg + 1) * gg - slarbs[0]) + '\n'
    w.write(answer)
    
    
r.close()
w.close()
print 'done'