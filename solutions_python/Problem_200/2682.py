# from sys import stdin

def is_tidy(s):
    return ''.join(sorted(s)) == s

n = input()
for i in xrange(1, n+1):
    N = input()
    for j in xrange(N, 0 , -1):
        if not is_tidy(str(j)):
            continue
        print 'Case #' + str(i) + ': ' + str(j)
        break

