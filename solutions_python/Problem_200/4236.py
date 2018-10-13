tc = input()

for t in range(tc):
    n = input()
    
    if n < 10:
        print "Case #" + str(t+1) + ": " + str(n)
        #print str(n) + " => " + str(n)
        continue

    s = list(str(n))
    i = 0
    while i < len(s)-1:
        if int(s[i]) > int(s[i+1]):
            s[i] = str(int(s[i]) - 1)
            for j in range(i+1, len(s)):
                s[j] = "9"
            i = 0
        else:
            i = i+1


    print "Case #" + str(t+1) + ": " + "".join(s).lstrip("0")
    #print str(n) + " => " + "".join(s).lstrip("0")

