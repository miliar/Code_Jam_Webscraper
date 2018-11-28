numcases = input()
for i in range(numcases):
    num = int(input())
    s = str(num)
    lastinc=0
    for j in range(1,len(s)):
        if int(s[j])<int(s[j-1]):
            rem = int(s[lastinc+1:])
            print "CASE #%d: %d"%(i+1,num-rem-1)
            break
        if int(s[j])>int(s[j-1]):
            lastinc = j
    else: print "CASE #%d: %d"%(i+1,num)
    
    