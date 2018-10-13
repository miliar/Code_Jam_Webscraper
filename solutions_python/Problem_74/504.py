import sys

file = open(sys.argv[1],'r')
testcase = int(file.readline())
for itest in range(1,testcase+1) :
    values = file.readline()
    
    list=values.split(' ')
    
    length = len(list)
    bindex=0;
    oindex=0;
    mindex=3;
    bpos=1;
    opos=1;
    next;

    time = 0

    blist=[]
    olist=[]

    for i in range(1,length,2):
        if list[i] == 'O':
            olist.append(int(list[i+1]))
        else:
            blist.append(int(list[i+1]))


    next = list[1]
    time=0
    ofin=0
    bfin=0
#    print "Start"
    while not(ofin == 1 and bfin == 1):
        time += 1
        #print "ITERATIN "+str(mindex)+" "+str(length)+" "+str(bfin)+" "+str(ofin)+next
        isp=0
        if len(blist) > bindex and bfin !=1: 
            if(bpos < blist[bindex]):
                bpos += 1
           #     print "a"
            elif(bpos > blist[bindex]):
                bpos -= 1
          #      print "b"
            elif(bpos == blist[bindex] and next == 'B'):             
         #       print "c"
                bindex += 1
                isp=1    
        
    
        if len(olist) > oindex and ofin !=1: 
            if(opos < olist[oindex]):
                opos += 1
        #        print "d"
            elif(opos > olist[oindex]):
                opos -= 1
       #         print "e"
            elif(opos == olist[oindex] and next == 'O' and isp != 1):
                isp = 1
                oindex += 1
       #         print "f"
        

        if mindex >= length+2:
           break
       
        if isp == 1 and mindex < length:
            
            next = list[mindex]
            mindex += 2
             
        if len(olist) <= oindex:
            ofin=1
        if len(blist) <= bindex:
            bfin=1
            
    print "Case #"+str(itest)+": "+str(time)


