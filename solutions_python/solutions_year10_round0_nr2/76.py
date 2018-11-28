tf = open("fair.in", "r")
tmp = tf.readline()
quesnum = int(tmp)
#print quesnum
for ques in range(1,quesnum+1):
    tmp = tf.readline()+" "
    n = int(tmp[:tmp.find(' ')])
#   print n
    tmp = tmp[tmp.find(' ')+1:]
    num = []
    for i in range(0,n):
        num.append(int(tmp[:tmp.find(' ')]))
        tmp = tmp[tmp.find(' ')+1:]
    num.sort(reverse=True)
#    print num
    for i in range(0,n-1):
        num[i] = num[i]-num[i+1]
#    print num
    ans = num[0]
    for i in range(1,n-1):
        if num[i]>0:
            b = num[i]
            t = ans%b
            while (t!=0):
                ans = b
                b = t
                t = ans%b
            ans = b
#    print ans
    print ("Case #%d: %d" % (ques, (ans-num[n-1]%ans)%ans));
