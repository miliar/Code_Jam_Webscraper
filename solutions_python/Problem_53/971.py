import re

stuff = open("A-small-attempt3.in").readlines()
case = 1
k = 1

while k<len(stuff):
    row = re.split(" ",stuff[k].rstrip())    
    row = map(int, row)
    
    a = []
    for x in range(row[0]):
        a.append([0,0])
    a[0][0] = 1

    # do snap times
    for j in range(row[1]):
        prev = a
        for i in range(row[0]):
            if i == 0:
                if a[i][1] == 0:
                    a[i][1] = 1
                else:
                    a[i][1] = 0
                #print a,"oka1"
            else:
                
                if prev[i][0] == 1:
                    if a[i][1] == 1:
                        a[i][1] = 0
                    else:
                        a[i][1] = 1
                if a[i-1][0] == 1 and a[i-1][1] == 1:
                    a[i][0] = 1
                else:
                    a[i][0] = 0
        #print a,"oka2",j
    if a[-1][0] == 1 and a[-1][1] == 1:
        print "Case #%d: ON" % case
    else:
        print "Case #%d: OFF" % case
    #print a
    k = k+1
    case = case + 1
