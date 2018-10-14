debug = False

out = open('out.txt', 'w')
lines = open('A-small-attempt0.in').read().splitlines()
   

def count_nei(string):
    letters = []
    count = []
    
    l = string[0]
    letters.append(l)
    count.append(1)
    
    for s in list(string[1:]):
        if l == s:
            count[-1] += 1
        else:
            l = s
            letters.append(l)
            count.append(1)
    
    return (letters, count)    

current = 1
T = int(lines[0])
for case in xrange(0, T):
    N = int(lines[current])
    current += 1
    if debug: 
        print "case", case+1, "-----------------------------------"
    strings = lines[current:current+N]
    if debug: print strings

    letters, counts = [], []
    for string in strings:
        t = count_nei(string)
        letters.append(t[0])
        counts.append(t[1])
    re = 0
    
    if debug:
        print letters
        print counts
    if all(x == letters[0] for x in letters[1:]):
        for i in xrange(len(counts[0])):
            column = [count[i] for count in counts]
            re += max(column)-min(column)
    else:
        re = "Fegla Won"
    current += N
    out.write("Case #%d: %s\n" % (case+1, str(re)))

print "DONE"
out.close()