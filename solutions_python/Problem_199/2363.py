def getHighestTidyBrute(n):
    currentDigit=0;
    arrn = list(map(int,str(n)))
    while not sorted(arrn) == arrn:
        n-=(arrn[len(arrn)-currentDigit-1]+1)*pow(10,currentDigit);
        arrn = list(map(int,str(n)))
        currentDigit+=1
    return n;

with open("B-large.in") as f:
    content=f.readlines()
content = [x.strip() for x in content]
f1=open("output2.out","w+")
T = int(content[0])
for i in range(1,T+1):
    f1.write("Case #" + str(i)+ ": " + str(getHighestTidyBrute(int(content[i])))+"\n")
f1.close()


    
        
    
