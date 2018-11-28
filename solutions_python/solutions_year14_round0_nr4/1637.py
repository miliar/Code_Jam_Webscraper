#def dwar(n, k, l):
#    return int(sum([(1 + (n[i] - k[i])/abs(n[i] - k[i])) for i in range(l)])/2)

def awar(n, k, l):
    i = 0
    j = 0
    count = 0
    while True:
        if k[j] > n[i]:
            j+=1
            i+=1
            count+=1
        else:
            i+=1
        if i==l or j==l:
            break
    return l-count

def run(FILE):
    infile = open(FILE, 'r')
    outfile = open('wars3.out', 'w')
    line1 = infile.readline()
    T = int(line1.strip('\n'))
    for i in range(T):
        l = int(infile.readline().strip('\n'))
        n = infile.readline().strip('\n').split(' ')
        k = infile.readline().strip('\n').split(' ')
        for j in range(l):
            n[j] = float(n[j])
            k[j] = float(k[j])
        n.sort()
        n.reverse()
        k.sort()
 #       d1 = dwar(n, k, l)
        k.reverse()
 #       d2 = dwar(n, k, l)
        aw = awar(n, k, l)
 #       d = max(d1, d2)
        d = l - awar(k, n, l)
        outfile.write('Case #' + str(i+1) + ': ' + str(d) + ' ' +str(aw) + '\n')
    infile.close()
    outfile.close()
        
