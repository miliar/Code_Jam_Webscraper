con = list("bcdfghjklmnpqrstvwxyz")

minlength = 1
def sub(string):
    return [string[start:start+length]
            for length in xrange(minlength, len(string) + 1)
            for start in xrange(len(string) - length + 1) ]

def count_em(string, integer):
    count_up = 0
    max = 0
    
    for x in string:
        if (x in con):
            count_up += 1
            if (max < count_up): max = count_up
        else:
            count_up = 0

        if (max == integer):
            return 1

    return 0

trials = int(raw_input())

for x in range(0, trials):
    line = raw_input().split()
    word = line[0]
    desire = int(line[1])
    
    count = 0
    subs = sub(word)
    
    for c in subs:
        count += count_em(c, desire)
    
    print "Case #"+str(x+1)+": "+str(count)