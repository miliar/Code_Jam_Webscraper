import string


def numoftops(values , p , S):
    tops = 0
    surp = 0
    for t in values:
        if t - max(2*(p-1),0) >= p:
            tops +=1
            continue
        if t - max(2*(p-2),0) >= p:
            surp += 1
            continue
    return tops + min([S,surp])



f = open("input","r")
file = f.readlines()



ctr = 0
for line in file:
    if ctr == 0:
        ctr += 1
        continue
    values = [ int(number) for number in string.split(line,' ')]
    N = values.pop(0)
    S = values.pop(0)
    p = values.pop(0)
    print "Case #" + str(ctr) + ":",  numoftops( values, p, S)
    ctr += 1
    
        
