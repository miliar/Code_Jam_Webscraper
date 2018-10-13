def should_add(s,p,ts):
    if(p == 0):
        return True,s
    if(ts == 0):
        return False,s
    d = int(ts/3)
    if(ts%3 == 0):
        if(d >= p):
            return True,s
        elif (d+1 >= p) and (s>0):
            return True,s-1
        else:
            return False,s
    elif ((ts-1)%3 ==0):
        if(d+1 >= p):
            return True,s
        else:
            return False,s
    else:
        if(d+1 >= p):
            return True,s
        elif(d+2>=p) and (s>0):
            return True,s-1
    return False,s

def score_calc(n,s,p,ts):
    sum = 0
    for i in range(0,n):
        flag,s = should_add( s, p, int(ts[i]) )
        if(flag):sum=sum+1
    return sum



file = open("b.txt","r")
raw = file.readlines()
final_score = ''
index = 0
for txt in raw:
    if index==0:
        nl = int(txt)
        index=index+1
    else:
        result = txt.rstrip('\n').split(' ')
        n = int(result[0])
        s = int(result[1])
        p = int(result[2])
        ts = result[3:]
        final_score = "Case #"+str(index)+": "+str(score_calc(n,s,p,ts))
        print final_score
        index = index+1