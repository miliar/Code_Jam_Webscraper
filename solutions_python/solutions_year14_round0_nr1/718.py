f = open("/Users/roshil/Desktop/onn","r")

q = open("output.txt","w")
q.truncate()
n = 0 
cost = 0
case = 1
dic = {}
for i in f:
    s = str(i)
  #  print i
  #  print len(i)
    if len(i) < 4:
        n = n+1
        print n
    if n%6 == 0 and n !=0:
        print dic
        top = len(dic.keys())
        cost = top/3*8
        if top%3 != 0:
            cost = cost + 5 + top%3
        q.write("Case #"+str(case)+": "+str(cost)+"\n")
        cost = 0
        case = case+1
        n = 2
        dic = {}
    if len(i) > 3:
        dic[i] = 1

q.close()