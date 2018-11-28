
def allplus(s):
    return (s.count("-") == 0)

def check(s, k):
    cnt = 0
    while len(s) > 0:
        if allplus(s):
            break
        elif s[0] == '+':
            s = s[1:]
        elif s[-1] == '+':
            s = s[:-1]
        elif k > len(s):
            return 'IMPOSSIBLE'
        else:
            cnt += 1
            for i in range(k):
                if s[i] == '-':
                    s[i] = '+'
                else:
                    s[i] = '-'
    return cnt
            


t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    (s, k) = line.split(' ')
    print "Case #{}: {}".format(i, check(list(s), int(k)))
