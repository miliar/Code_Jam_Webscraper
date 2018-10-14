


f = open('C:\\Users\Bruce\Downloads\A-large.in')
content = f.readlines()
raw = [x.strip() for x in content]

ntestcase=int(raw[0])
cases=raw[1:]

def swapPancake(var1):
    if var1=="+":
        var2="-"
    else:
        var2="+"
    return var2

olist=[]

for i in range(ntestcase):
    cake=list(cases[i].split()[0])
    flip=int(cases[i].split()[1])
    count=0
    answer=""
    for i in range(len(cake)):
        while i <= (len(cake) - flip):
            if cake[i]=="-":
                for j in range(flip):
                    cake[i+j]=swapPancake(cake[i+j])
                count+=1
            break
    if "-" in cake:
        answer="IMPOSSIBLE"
    else:
        answer=str(count)
    olist.append(answer)

with open('P1L.txt','w') as file:
    for i in range(ntestcase):
        file.write("Case #" + str(i+1) +": " + olist[i] + '\n')