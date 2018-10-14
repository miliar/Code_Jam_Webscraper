#!/usr/bin/env python

#infile = "B-large.in"
infile = "B-small-attempt1.in"
#infile = "B-sample.in"
outfile = infile.split(".")[0] + ".out"

fin = open(infile, "r")
fout = open(outfile, "w")

TC = int(fin.readline())

for tc in range(TC):

    P = int(fin.readline())
    M = [int(value) for value in fin.readline().split()]
    rounds = []
    for i in range(P):
        round = [int(value) for value in fin.readline().split()]
        rounds.append(round[:])
    
    #print P, rounds
    
    def get_prices(i):
        prices = []
        for p in range(P):
            prices.append(rounds[p][i/(2**(p+1))])
        return prices
    
    def buy_ticket(i, p):
        buy = rounds[p][i/(2**(p+1))]
        rounds[p][i/(2**(p+1))] = 0
        return buy

        
    #if tc == 2:
    #    import pdb
    #    pdb.set_trace()

    price = 0
    i = 0
    for m in M:
        for p in range(m, P):
            price += buy_ticket(i, p)
        i += 1


    res = "Case #%s: %s" %(tc+1, price) 
    
    res += '\n'
    print res,
    fout.write(res)
    #raw_input('')

fin.close()
fout.close()
