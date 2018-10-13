inputfile = "B-large.in"
outputfile = "output.out"

output = ""

def timevalue(t):
    hours = int(t[0:2]) * 60
    minutes = int(t[3:5])
    return hours + minutes

def minutesvalue(m):
    return m


fi = file(inputfile)
data = fi.read()
fi.close()

lines = data.split("\n")

cindex = 1

cases = int(lines[0])



for i in range(1,cases + 1):
    Amust = []
    Bmust = []

    Aarrives = []
    Barrives = []
    
    
    resttime= minutesvalue(int(lines[cindex]))
    temp = lines[cindex + 1]
    temp2 = temp.split(" ")
    NA = int(temp2[0])
    NB = int(temp2[1])

    cindex += (2)

    for k in range(0,NA):
        temp = lines[cindex]
        temp2 = temp.split(" ")
        Amust.append(timevalue(temp2[0]))
        Barrives.append(timevalue(temp2[1]) + resttime)
        cindex+= 1

    for k in range(0,NB):
        temp = lines[cindex]
        temp2 = temp.split(" ")
        Bmust.append(timevalue(temp2[0]))
        Aarrives.append(timevalue(temp2[1]) + resttime)
        cindex+= 1

    AmustT = Amust[:]
    BmustT = Bmust[:]

    # Processing A
    AmustT.sort()
    Aarrives.sort()
    AmustT.reverse()

    for T1 in range(len(Aarrives) - 1,-1,-1):
        for T2 in range(len(AmustT) - 1,-1,-1):
            if Aarrives[T1] <= AmustT[T2]:
                Aarrives.pop(T1)
                AmustT.pop(T2)
                break
            
    
    # Prcessing B
    BmustT.sort()
    Barrives.sort()
    BmustT.reverse()

    for T1 in range(len(Barrives) - 1,-1,-1):
        for T2 in range(len(BmustT) - 1,-1,-1):
            if Barrives[T1] <= BmustT[T2]:
                Barrives.pop(T1)
                BmustT.pop(T2)
                break
  

    output += "Case #"+str(i)+": " + str(len(AmustT)) + " " + str(len(BmustT)) + "\n"


file2 = file(outputfile,"w")
file2.write(output)
file2.close()

    

    
        
        

