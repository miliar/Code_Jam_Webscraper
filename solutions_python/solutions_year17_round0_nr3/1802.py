t=  int(raw_input())

for i in xrange(t):
    n, k = map(int, raw_input().strip().split(' '))
    available = [(0,n-1)]
    
    for x in xrange(k):
        choices = []
        for index, bound in enumerate(available):
            middle = (bound[1] + bound[0]) / 2
            maximum = min(bound[1] - middle, middle - bound[0])
            minimum = max(bound[1] - middle, middle - bound[0])
            choices.append((maximum, minimum, -middle, index))
        choices.sort(reverse=True)

        index = choices[0][3]
        start, end = available.pop(index)
        middle = -choices[0][2]
        if middle != start:
            available.append((start,middle-1))
        if middle != end:
            available.append((middle+1, end))
    print 'Case #{0}: {1} {2}'.format(i+1, choices[0][1],choices[0][0])