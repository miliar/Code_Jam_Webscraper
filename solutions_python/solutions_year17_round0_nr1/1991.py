f = open('in.txt','r')
fo = open('out.txt','w')
cases = int(f.readline());
curcase=1
while curcase<=cases:
    s,k = f.readline().split()
    k = int(k)
    count = 0
    minus = 0
    flag = True
    c = [x for x in s]
    i = 0
    while i<len(c):
        if(c[i] == '+'):
            i += 1
            continue
        else:
            if(len(c) - i < k):
                flag = False
                break
            j = 0
            while j<k:
                if(c[i+j] == '+'):
                    c[i+j] = '-'
                else:
                    c[i+j] = '+'
                j += 1
            count += 1
        i += 1
    if(flag):
        fo.write("Case #" + str(curcase) + ": " +str(count) + "\r\n")
        print("Case #" + str(curcase) + ": "+ str(count))
    else:
        fo.write("Case #" +str(curcase)+ ": "  + "IMPOSSIBLE\r\n")
        print("Case #" + str(curcase) + ": IMPOSSIBLE")
    curcase += 1
fo.close()
