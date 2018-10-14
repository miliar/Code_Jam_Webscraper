data = open("input.in","r")
output = open("output.txt","w")
count = int(data.readline())
ans = []
for i in range(1,count+1):
    ans.append(int(data.next()))    
    line1 = []
    for lineid in range(ans[0]):
        line = data.next()
    line1.append(map(int,list(line.split(" "))))
    for skip in range(4-ans[0]):
        data.next()
    ans.append(int(data.next()))    
    for lineid in range(ans[1]):
        line = data.next()
    line1.append(map(int,list(line.split(" "))))
    for skip in range(4-ans[1]):
        data.next()    
    resultset = list(set(line1[0]).intersection(set(line1[1])))
    if(len(resultset) == 1 ):
        output.write("\nCase #%d: %d"%(i,resultset[0]))
    elif( len(resultset) == 0):
        output.write("\nCase #%d: Volunteer cheated!"%i)
    else:
        output.write("\nCase #%d: Bad magician!"%i)
    ans = []
    line1 = []
    line = ""
output.close()
data.close()
    
    
