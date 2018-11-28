def dancing(scores,best,surprising):
    answer=0
    for each in scores:
        if each<best:
            continue
        if each>=(best*3)-2:
            answer=answer+1
        elif each>=(best*3)-4:
            if surprising>0:
                surprising=surprising-1
                answer=answer+1
    return str(answer)

print dancing([8,0],1,1)


x=open("test4.in")
z=open("output.txt","w")

case=0
currentline=x.readline()


currentline=x.readline().rstrip().lstrip().split()
while currentline:
    case=case+1
    surprising=int(currentline[1])
    best=int(currentline[2])
    scores=map(int,currentline[3:])
    z.write("Case #"+str(case)+": "+dancing(scores,best,surprising)+"\n")
    currentline=x.readline().rstrip().lstrip().split()
z.close()

