import heapq

for case in range(int(raw_input())):
    values = map(int, raw_input().split())
    L, t, N, C = values[:4]

    orig = values[4:]
    assert len(orig) == C

    distances = orig * (N/len(orig)+1)
    distances = distances[:N]
    tag = [False]*N
    assert len(distances) == N

    time = 0

    #find t
    i=0
    while i < N and time < t:
        time += distances[i] * 2
        i+=1
    if time > t:
        i-=1
        time -= distances[i] * 2
        left = t-time
        time += left

        distanceToMove = left / 2.0
        distances[i] -= distanceToMove
    distances=distances[i:]

    for j in range(L):
        m=0
        for k in range(len(distances)):
            if tag[k]:
                continue
            if distances[k]>distances[m]:
                m=k
        tag[m]=True
        distances[m]=distances[m]/2.0

    time+=sum(distances)*2


    print 'Case #%d: %d' % (case+1, int(time))
