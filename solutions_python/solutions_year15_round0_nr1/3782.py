f= open("A-small-attempt0.in","r")
data = f.read().splitlines()
print data


output = open("output.txt", "w")
counter = 0
d1 = data[counter]
for b in range(100):
    d1 = data[counter]
    x = d1[0]
    y = d1[2:]
    friends = 0
    a = 0
    for s in range(int(x)+1):
        if s>0:
            a = a+int(y[s-1])
            if y[s] != "0":
                if a<s:
                    x= s-a
                    a += x
                    friends += x
    counter +=1
    print friends
    result = "Case #"+str(counter)+":"+" "+str(friends)
    output.write(result+"\n")

    
    



#result = "Case #"+str(counter)+":"+" "+str(friends)
#output = open("outputtest.txt", "w")
#output.write(result)
output.close()
