fin = open("B-large.in","r")
fout = open("B-large.out","w")
row = 0
TestCases = int(fin.readline())
for line in fin:
    string = ""
    row += 1
    print "Case #%d: " %(row),
    string += "Case #" + str(row) + ": " 
    count  = 0
    list = line.split(" ")
    googlers = int(list[0])
    surprising  = int(list[1])
    best = int(list[2])
    for x in xrange(googlers):
        flag =0
        total = int(list[3+x])
        print "processing for : ", total,
        if total >= best:
            total = total-best
            if total >= 2*(best-1):
                count += 1
                print "Counted"
            elif total >= 2*(best -2) and surprising > 0:
                count += 1
                surprising -= 1
                print "Counted"
                
    print count   
    string += str(count) + "\n"         
    fout.write(string)
fout.close()
                    
                
        

            
        
          