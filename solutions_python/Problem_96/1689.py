read = []

def get_input() :
    while not read:
        read.extend(map(int,raw_input().split()))

    ret = read[0]
    read.pop(0)
    return ret


t = input()
for i in xrange(t):
    n,s,p=[get_input() for x in '123']

    surp = 0
    cnt = 0
    for j in xrange(n):
        this = get_input()
        if (this+2)/3 >= p: cnt += 1
        elif p<=this and p - (this-p)/2 == 2: surp += 1

    print "Case #%d:" % (i+1), min(surp,s)+cnt