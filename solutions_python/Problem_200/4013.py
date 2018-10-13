# Problem B

with open('B-small-attempt0.in.txt','r') as f:
    k = f.readline()
    for i in range(int(k)):
        n = f.readline()
        n = n.strip()
        n = n[::-1]
        pre = 9
        count = 0
        tail = ''
        for c in n:
            if (pre < 0):
                tail =  (str(int(c) - 1) if ((int(c) - 1) >0) else '') + '9' * count
                pre = int(c) - 1
            elif (int(c) <= pre):
                pre = int(c)
                tail = c + tail
            else:
                tail = (str(int(c) - 1) if ((int(c) - 1) >0) else '') + '9' * count
                pre = int(c) - 1
            count +=1
        print "Case #"+ str(i+1) + ": " + tail
