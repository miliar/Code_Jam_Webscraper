def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
 
def intersect(seq1, seq2):
    res = []                     # start empty
    for x in seq1:               # scan seq1
        if x in seq2:            # common item?
            res.append(x)        # add to end
    return res

def main():
    ifile = open('input.txt', 'r')
    ofile = open('output.txt', 'w')
    n = int(ifile.readline())
    for i in range(0, n):
        a, b, p = map(int, ifile.readline().split(' '))
        d = {}
        for j in xrange(p, b/2):

            if isprime(j):
                kl = j
                for k in d.keys():
                    if (a / (k*j) != b /(k*j)) or a % (k*j) ==0  or b % (k*j) == 0:
                        kl = k
                        #print kl
                        break
                l = []
                for x in xrange(a, b + 1):
                    if x % j == 0:
                        l.append(x)
                if len(l) > 1:
                    if kl in d.keys():
                        for el in l:
                            if not el in d[kl]:
                                d[kl].append(el)
                    else:
                        d[kl] = l
        c = 0
        #print d
        for v in d.values():
            c += len(v) - 1
        res = b-a+1-c
        print res
        ofile.write('Case #%i: %i' %(i+1, res))
        if i != (n - 1):
            ofile.write('\n')
        
    ofile.close()
    print 'done'

if __name__ == '__main__':
  main()