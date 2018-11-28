T = int(raw_input())
for t in range(1,T+1):
    line =  str(raw_input()).split(" ")

    if len(line[0]) == 1 and len(line[1]) == 1 :
        print "Case #"+ str(t)+ ": 0"
    else:
        A = line[0]
        B = line[1]
        res = 0
        #print range(int(A),int(B)+1)
        for i in range(int(A),int(B)+1):
            n = str(i)
            m = str(i)
            for j in range(0, len(str(i))-1):
                m = m[-1]+m[0:-1]
                if (int(A) <= int(n)) and (int(n) < int(m)) and (int(m) <= int(B)):
                    res = res + 1
    
        print "Case #"+ str(t)+ ": " + str(res)
