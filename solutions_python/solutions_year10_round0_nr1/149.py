def snap(snappers):
    for i in xrange(len(snappers)):
        snappers[i] = not snappers[i]
        if snappers[i]:
            break

def naive(K, N):
    #if N == 0:
    #    return True
    snappers = [False] * N
    for k in xrange(K):
        snap(snappers)
    for s in snappers:
        if not s:
            return False
    return True

infile = file("A-large.in")
num_cases = int(infile.readline())

for case_num in xrange(num_cases):
    N, K = map(int, infile.readline().split())
    target = (1 << N) - 1
    is_on = (K & target) == target

    if is_on:
        answer = "ON"
    else:
        answer = "OFF"
    print "Case #%d: %s" % (case_num + 1, answer)
