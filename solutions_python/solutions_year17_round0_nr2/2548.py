def checktidy(digitlist):
 #   numstr = ''.join(map(str,digitlist))
 #   print "is " + numstr +"tidy? "

    for i in xrange(len(digitlist)-1):
        if(digitlist[i]<= digitlist[i+1]):
            continue
        else:
            return False
    return True

def findmax(digitlist):
    numstr = ''.join(map(str,digitlist))
  #  print "is " + numstr +"tidy? " + str(checktidy(digitlist))

    if(checktidy(digitlist)):
        #print "returning " + numstr
        return numstr
    
    digitlist = [ int(x) for x in digitlist ]

    noofdigits = len(digitlist)
    
    #print "digitlist" + str(digitlist)
   # print "noofdigits" + str(noofdigits)
    maxnum = []
    for i in xrange(len(digitlist)-1):
        
        if(digitlist[i]<= digitlist[i+1]):
            maxnum.append(digitlist[i])
        else:
            maxnum.append(digitlist[i]-1)
            break
        
    for i in xrange(len(digitlist) - len(maxnum)):
        maxnum.append(9)

   # print maxnum
    if(maxnum[0] == 0):
        maxnum.pop(0)

    check = checktidy(maxnum)
    while(check == False):
        digitlist = maxnum
        maxnum = []
        for i in xrange(len(digitlist)-1):
            
            if(digitlist[i]<= digitlist[i+1]):
                maxnum.append(digitlist[i])
            else:
                maxnum.append(digitlist[i]-1)
                break
            
        for i in xrange(len(digitlist) - len(maxnum)):
            maxnum.append(9)

        if(maxnum[0] == 0):
            maxnum.pop(0)
        
        check = checktidy(maxnum)    
    
    return maxnum
        

myfile = open("B-large.in", "r") 
noofcases = myfile.readline();
outfile = open("B-large.out", 'w')
for i in range(int(noofcases)):
    myinput = myfile.readline();
    
    digitlist = list(myinput)    
    digitlist.pop()
    returnval = findmax(digitlist)
    
    numstr = ''.join(map(str,returnval))
    outfile.write("Case #" + str(i+1) + ": " + numstr+"\n" )  # python will convert \n to os.linesep

outfile.close()
