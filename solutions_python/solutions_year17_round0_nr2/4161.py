t=int(raw_input().strip())
for k in range(t):
    y = raw_input()
    x = list(y)
    z=x[0]
    ind, index = 0, 0
    same = False
    val = str(z)
    if len(x) > 1:
        for i in range(1,len(x)):
            if x[i] > z :
                z=x[i]
                val = y[:i+1]
                same = False
                ind = i
            elif x[i] == z :
                same = True
                index = i
            else :
                same = False
                break
        if same and x[ind] == x[index] :
            val = y
        else :
            l = len(x) - len(val)
            if l != 0 :
                val = str(int(val) - 1)
            val = val + ('9' * l)
    print "Case #" + str(k+1) + ":",
    print int(val)
