
def case(s , i ) :
    claps = 0
    needToAdd = 0
    
    m, data = s.split(" ")
    
    for j in range(int(m)+1):
        temp = int(data[j])
        if claps < j and temp > 0  :
            addNow = j - claps 
            
            needToAdd += (addNow)
            claps += addNow
        
        claps += temp
    



    return "Case #" + str(i) + ": " + str(needToAdd)




w = open("A-large.in")
o = open("output.txt","w")
t= int(w.readline()[:-1])
for i in range(t):
    line = w.readline()
    if (line[-1] == "\n"):
        line = line[:-1]
    toWrite  = case( line, i +1)
    print(toWrite)
    o.write(toWrite+"\n")


w.close()
o.close()

