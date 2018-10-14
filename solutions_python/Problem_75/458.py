myfile=open("B-large.in", "r")
inp=myfile.read().split("\n")

fullanswer=""
i=0
for casenumber in range(int(inp[0])):

    i+=1
    var=inp[i].split(" ")
    p=0
    comb=[]
    for q in range(int(var[p])):
        p+=1
        comb.append(var[p])
        
    inv=[]
    p+=1
    for q in range(int(var[p])):
        p+=1
        inv.append(var[p])
        
    p+=2
    work=var[p]
    leng=len(work)

    workc=work
    elements=[]
    for q in workc:

        elements.append(q)

        if len(elements)>1:
            
            tempcombo=q+elements[len(elements)-2]
            for w in comb:
                if tempcombo in w[:-1]:
                    elements.pop()
                    elements.pop()
                    elements.append(w[2])

                elif len(elements)>=2 and tempcombo[::-1] in w[:-1]:

                    elements.pop()
                    elements.pop()
                    elements.append(w[2])


            for w in inv:
                
                tempelements=elements[:]
                count=0
                if w[0] in tempelements:
                    tempelements.remove(w[0])
                    count+=1
                if w[1] in tempelements:
                    tempelements.remove(w[1])
                    count+=1
                if count==2:

                    elements=[]
    s="["
    ki=0
    l=len(elements)
    for ele in elements:
        

        if ele != "'":
            s+=(ele)
        if ki != l-1:

            s+=", "
        ki+=1
    s+="]"
    fullanswer+="Case #%d: %s\n" % (casenumber+1,s)


results=open("B.out","w")
results.write(fullanswer)
myfile.close()
results.close()
