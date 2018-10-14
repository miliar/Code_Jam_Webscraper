
def GCF_two(a, b):
    ''' Euclidean algorithm '''
    while b:
        a, b = b, a % b
    return a

def LCM_two(a, b):
    return a / GCF_two(a, b) * b

def GCF(num):
    return reduce(GCF_two, num)

def LCM(num):
    return reduce(LCM_two, num)



f = open("C-small-attempt0.in", 'r')
data = f.readlines()
f.close()

data = map(str.strip, data)
data = zip(data[1::2], data[2::2])

out = []
iterator = 0
for rec in data:
    iterator += 1
    row1 = rec[0].split(' ')
    row1 = map(int, row1)
    row2 = rec[1].split(' ')
    row2 = map(int, row2)
    
    minfreq = row1[1]
    maxfreq = row1[2]
    
    for freq in range(minfreq, maxfreq+1):
        # print "trying", freq
        found = []
        for others in row2:
            # print "  with", others
            # print (freq % others), (others % freq)
            if (freq % others == 0 or others % freq == 0):
                found.append(True)
        if len(found) == len(row2):
            # print found
            break
    if len(found) == len(row2):
        out.append("Case #%d: %d" % (iterator, freq))
    else:
        out.append("Case #%d: NO" % (iterator))

f = open('C-small-attempt0.out', 'w')
f.write('\n'.join(out))
f.close()