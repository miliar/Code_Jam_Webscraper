
def remove(s, digit, count):
    rv = s
    for ch in digit:
        #print "replacing " + ch + " in " + rv + " " + str(count) + " times"
        rv = rv.replace(ch, '', count)
    return rv

def process(ss):
    num = [0]*10
    s = ss

    num[0] = s.count('z')
    s = remove(s, 'zero', num[0])

    num[2] = s.count('w')
    s = remove(s, 'two', num[2])

    num[6] = s.count('x')
    s = remove(s, 'six', num[6])
    
    num[4] = s.count('u')
    s = remove(s, 'four', num[4])
     
    num[1] = s.count('o')
    s = remove(s, 'one', num[1])

    num[3] = s.count('r')
    s = remove(s, 'three', num[3])

    num[8] = s.count('t')
    s = remove(s, 'eight', num[8])

    num[5] = s.count('f')
    s = remove(s, 'five', num[5])

    num[7] = s.count('v')
    s = remove(s, 'seven', num[7])

    num[9] = s.count('n')/2
    s = remove(s, 'nine', num[9])

    rv = ''
    for i in range(10):
        rv += str(i)*num[i]
    return rv

t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    #print line
    print("Case #{}: {}".format(i, process(line.lower())))
