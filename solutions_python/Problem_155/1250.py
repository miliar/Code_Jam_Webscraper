finput= open('A-large.in')
fout= open('A-large.out', 'w')

ntc= int(finput.readline())

for y in xrange(0, ntc):
    inps= finput.readline()
    #print (str(inps))
    #inputs= raw_input()
    inp_lists= map(str, inps.split(' '))

    #print "second part is " + inp_lists[1].strip()
    
    #print "len gives " + str(len(inp_lists[1].strip()))
    
    second= str(inp_lists[1].strip())
    #shymeter= map(int, second.split())
    shymeter= [ int(x) for x in second ]

    sum_prevs= shymeter[0]
    extra=0
    extrafin=0

    #print "length of second part is " +str(len(shymeter))
    
    for x in xrange(1,len(shymeter)):


        if (shymeter[x] >0):
            if (x > sum_prevs):
                #print "x is" + str(x)
                #print "sum_prevs is "+ str(sum_prevs)
                extra= (x - sum_prevs)
                extrafin += extra
                #print "extrafin is" +str(extrafin)
                #print "extra is " + str(extra)
            else:
                extra=0
            sum_prevs= sum_prevs + shymeter[x] + extra
            #print "sum prevs is "+ str(sum_prevs)
            

        #sum_prevs= sum_prevs + shymeter[x]
        #print str(x)
        #print str(sum_prevs)
        

    if (y == ntc-1):
            fout.write("Case #" + str(y+1) + ": " + str(extrafin).strip())
    else:
        fout.write("Case #" + str(y+1) + ": " + str(extrafin).strip() +"\n")
    #print "final is "+ str(extrafin)
        
fout.close()
