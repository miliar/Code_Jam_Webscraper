# looking for maximum possible y
# only mod3 <= 2 eligible  
# case sssm
# standard = 5
# 3 3 3 0 -> 225(*)
# 3 3 3 1 -> 224 e
# 4 4 4 2 -> 235(*)

def mod3(n):
    return n%3

def castInt(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

q = open('q.txt' , 'r')
a = open('a.txt' , 'w')
c = 0
for line in q:
    c+=1
    y = 0
    goodResult = []
    badResult = []
    okResult = []
    query = castInt(line.strip().split(' '))
    surprise = query[1]
    standard = query[2]
    query = query[3:]
    for qu in query:
        m = mod3(qu)
        avgScore = (qu-m)/3
        if avgScore >= standard:
            goodResult.append([qu,avgScore,m])
        elif avgScore+1 == standard and m!=0:
            goodResult.append([qu,avgScore,m])
        elif avgScore == 0 and standard != 0:
            badResult.append([qu,avgScore,m])
        elif avgScore+2 == standard and m==2:
            okResult.append([qu,avgScore,m])
        elif avgScore+1 == standard and m==0:
            okResult.append([qu,avgScore,m])
        else:
            badResult.append([qu,avgScore,m])
    #5
    # 233 , 22
    # 444 

    #first fulfill the surprise condition
    if len(okResult) > surprise:
        #bad , without surprise , OK cant become Y
        y = surprise+len(goodResult)
    else:
        #good , surprise cover all OK to be Y
        y = len(okResult)+len(goodResult)
    
    a.write("Case #"+str(c)+": "+str(y)+"\n")
    print str(c)+'----------------'+str(y)
    print query
    print surprise
    print standard
    print okResult
    print goodResult
    print badResult
        

q.close()
a.close()
