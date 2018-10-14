def maximum(score, surprising):
    if score==0:
        return 0
    if not surprising:
        if score%3==0:
            return int(score/3)
        else:
            return int(score/3)+1
    else:
        if int(score/3)*3+2==score:
            return int(score/3)+2
        else:
            return int(score/3)+1


def solve(scores,nb_s, least):
    scores.sort()
    scores.reverse()
    cnt=0
    for i in range(len(scores)):        
        if scores[i]>=3*least-2:
            if maximum(scores[i],False)>=least:
                cnt=cnt+1
        else:
            if nb_s>0:
                if maximum(scores[i],True)>=least:
                    cnt=cnt+1
                nb_s=nb_s-1
            else:
                if maximum(scores[i],False)>=least:
                    cnt=cnt+1        
    return cnt

f=open("B-large.in","r")
lines=f.readlines()
f.close()

results=[]

N=eval(lines[0])
for i in range(N):
    temp=lines[i+1].split()
    temp=list(map(eval,temp))
    result=solve(temp[3:],temp[1],temp[2])
    results.append("Case #"+str(i+1)+": "+str(result)+"\n")
    print(str((i+1)/N))

f=open("o.txt","w")
f.writelines(results)
f.close()
    

