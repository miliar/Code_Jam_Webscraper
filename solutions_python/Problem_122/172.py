
def solve(N, numbers, products, infile, outfile):
    print 'numbers :', numbers, 'products:', products, 'N:', N
    
    for prod in products:
        possible = set()
        for num in numbers:
            if prod % num == 0:
                possible.add(num)
        
        def set_contains(item):
            return item in possible
        filter(set_contains, numbers)
    
    print 'possible:', numbers
    
    res = [ numbers[0] for a in xrange(N) ]  # @UnusedVariable
    
    debug = False
    
    if debug:
        sr = ''
        for r in res: sr = sr + str(r)
        print 'res.0:', sr
    
    for prod in products:
        idx = 0
        while prod > 1:
            if debug:
                sr = ''
                for r in res: sr = sr + str(r)
                print 'res.P:', sr, 'prod:', prod,
            
            found = False
            for i in xrange(idx, N):
                if prod % res[i] == 0:
                    if debug: print '+', i
                    prod = prod / res[i]
                    found = True
                    break
                
            if found:
                idx += 1
            else:
                if debug: print '-', idx
                for n in numbers:
                    if prod % n == 0:
                        prod = prod / n
                        res[idx] = n 
                        idx += 1
                        break
    
    sr = ''
    for r in res: sr = sr + str(r)
    print 'res.F:', sr
    
    outfile.write('\n' + sr)

def read(R, N, M, K, infile, outfile):
    numbers = []
    for n in xrange(M, 1, -1):
        numbers.append(n)
    
    for r in xrange(R):  # @UnusedVariable
        prod = []
        for snum in infile.readline().split(' '):
            num = int(snum)
            if num > 1: 
                prod.append(num)
        prod.sort(reverse=True)
        solve(N, numbers, prod, infile, outfile)
    
if __name__ == '__main__':
    with open('../c.in', 'r') as input_file:
        input_file.readline() # Cases == 1
        with open('../c.out', 'w') as output_file:
            output_file.write('Case #1:')
            
            sr, sn, sm, sk = input_file.readline().split(' ')
            read(int(sr), int(sn), int(sm), int(sk), input_file, output_file)
