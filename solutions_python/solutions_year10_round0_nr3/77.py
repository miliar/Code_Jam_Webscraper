T = int(raw_input())

for t in xrange(T):
    R, k, N = map(int, raw_input().split(' '))
    gs = map(int, raw_input().split(' '))

    # Function to fill the cart based on
    # the current group waiting
    def fillout(queue):
        groups = gs[queue:] + gs[:queue]
        people = 0
        for (i, gi) in enumerate(groups):
            people += gi
            if (people > k):
                people -= gi
                break
        return (people, (queue+i)%len(gs))


    # Iterate while trying to find a cycle
    step = 0
    queue = 0
    cycles = []
    gains = []

    while step < R:
        cycles.append(queue)
        (people, queue) = fillout(queue)
        gains.append(people)
        step += 1

        if queue in cycles:
            break


    benefits = sum(gains)
    if step < R:
        index = cycles.index(queue)
        gains = gains[index:]

        benefits += ((R-step)/len(gains)) * sum(gains)
        benefits += sum(gains[:(R-step)%len(gains)])

    print "Case #%d: %d" % (t+1, benefits)
