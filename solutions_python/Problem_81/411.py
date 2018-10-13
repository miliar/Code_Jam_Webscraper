#PROBLEM 1A


#get file
raw = open("D:\choses\\A-large.in") #change
inputstream = raw.readlines()
raw.close()
#output
output = open("D:\choses\output-Al.out","w")


print("There are "+str(inputstream[0][:-1])+" test cases")


def rpi(wp,owp,oowp):
    return 0.25*wp + 0.50*owp + 0.25*oowp

linecount = 1
def handle(thing): #TWEAK THIS FUNCTION MAJORLY
    global linecount
    games = []
    for i in range(1,int(inputstream[linecount])+1,1):
        games.append(list(inputstream[linecount+i]))
    for i in range(0,len(games),1):
        if(games[i][-1] == '\n'):
            games[i] = games[i][:-1]
    result = []
    teams = [[0,0,0,0,0,0] for x in range(len(games))]
    for i in range(0,len(games),1):
        wp = 0
        owp = 0
        oowp = 0
        wincount = 0
        playcount = 0
        for j in range(0,len(games[i]),1):
            if games[i][j] == "1":
                wincount+=1
                playcount+=1
            elif games[i][j] == "0":
                playcount+=1
        teams[i][0] = float(wincount)/playcount #wp
        teams[i][4] = playcount
        teams[i][5] = wincount
    owps = []
    for i in range(0,len(games),1):
        owps=[]
        for j in range(0,len(games),1):
            if(games[j][i]=="0"):
                owps.append(float(teams[j][5])/(teams[j][4]-1))
            elif(games[j][i]=="1"):
                owps.append(float(teams[j][5]-1)/(teams[j][4]-1))
        working = 0
        for item in owps:
            working += item
        print("HEY")
        print(owps)
        teams[i][1] = float(working)/len(owps)

    for i in range(0,len(games),1):
        working = 0
        sizeof = 0
        for count in range(0,i,1):
            if(games[i][count]!="."):
                working+=teams[count][1]
                sizeof+=1
        for count in range(i+1,len(games),1):
            if(games[i][count]!="."):
                working+=teams[count][1]
                sizeof+=1
        teams[i][2] = float(working)/(sizeof)

    for i in range(0,len(games),1):
        result.append(rpi(teams[i][0],teams[i][1],teams[i][2]))
    linecount+=int(thing)+1
    print(teams)
    return result



count = 1
while(count<=int(str(inputstream[0][:-1]))):
    result = handle(inputstream[linecount])
    output.write("Case #"+str(count)+": \n")
    for i in range(0,len(result),1):
        output.write(str(result[i]))
        output.write("\n") #AND THIS LINE
    count+=1
#for line in inputstream:
    #print(line)


output.close()