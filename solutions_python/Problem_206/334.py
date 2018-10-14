def solve(test):
    # N = input()
    dd, n = map(int, raw_input().split())

    d = float(dd)

    k = [0] * n
    s = [0] * n

    for i in xrange(n):
        k[i], s[i] = map(float, raw_input().split())

    
    t = [ (d-k[i])/s[i]  for i in xrange(n)]

    print d/max(t)

    #print result


def create_array(*sizes):
   return [0 if len(sizes)==1 else create_array(*sizes[1:]) for x in xrange(sizes[0])]




import sys
sys.stdin = open(sys.argv[1] if len(sys.argv) > 1 else "sample.in")

for test in range(input()):
    print "Case #{}:".format(test+1),
    answer = solve(test)
    if answer != None:
        print answer


