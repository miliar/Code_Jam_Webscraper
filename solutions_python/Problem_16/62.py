INPUT = 'D-small-attempt1.in'
#INPUT = 'input.in'
#INPUT = 'A-large.in'
OUTPUT = INPUT.replace('.in', '.out')

f = open(INPUT, 'r')
input = f.readlines()
f.close()
N = eval(input[0])
input = input[1:]

f = open(OUTPUT, 'w')

def create_perms(perms, p, ind, k):
    if ind == k:
        perms.append(p)
    for i in xrange(k):
        if not i in p:
            tmp = list(p)
            tmp.append(i)
            create_perms(perms, tmp, ind+1, k)

def compress(p, k, s):
    tmp = ''
    for block in xrange(len(s)/k):
        for i in xrange(k):
            tmp += s[block*k + p[i]]
    count = 1
    for i in xrange(len(tmp) - 1):
        if tmp[i] != tmp[i+1]:
            count += 1
    return count
    
case = 0
i = 0
while case < N:
    case += 1
    k = eval(input[i].strip())
    i += 1
    s = input[i].strip()
    i += 1
    perms = []
    create_perms(perms, [], 0, k)
    #print perms
    ans = len(s)
    for p in perms:
        tmp = compress(p, k, s)
        if tmp < ans:
            ans = tmp
    print 'Case #%d: %d' % (case, ans)
    f.write('Case #%d: %d\n' % (case, ans))
    
f.close()
