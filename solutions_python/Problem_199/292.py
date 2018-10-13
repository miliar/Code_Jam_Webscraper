
def calculate(string, size):
    counter = 0
    for i in xrange(len(string)):
        if string[i] == '+':
            continue
        if len(string) < i + size:
            return -1
        counter += 1
        for j in xrange(i, i + size):
            string[j] = '+' if string[j] == '-' else '-'
    return counter

cases = int(raw_input())
for i in xrange(1, cases+1):
    st, s = raw_input().split(' ') 
    size = int(s)
    string = list(st)
    counter = calculate(string, size)
    if counter >= 0:
        print 'Case #%d: %d' % (i, counter)
    else:
        print 'Case #%d: IMPOSSIBLE' % (i)

