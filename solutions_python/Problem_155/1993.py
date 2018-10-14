import sys

f = open(sys.argv[1],"r")

valid = False
linenum = 0

for line in f:
    if not valid:        
        valid = True
    else:
        linenum += 1
        line = line.replace("\n","")
        arr = line.split(" ")
        total = int(arr[0])
        ss = arr[1]
        length = len(ss)
        count = 0
        need = 0
        totalneed = 0
        for i in range(length):
            aud = int(ss[i])
            if i == 0:
                count += aud
            elif count >= i:
                count += aud
            else:
                need = i - count
                totalneed += need
                count += aud + need
        print "Case #%d: %d" % (linenum, totalneed)
            
