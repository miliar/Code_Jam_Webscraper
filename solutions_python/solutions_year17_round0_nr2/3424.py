f = open("B-large.in","r").readlines()
g = open("B-large.txt",'w')
testcases = int(f[0])

for j in range(1,testcases+1):
    n = f[j].strip()
    li = list(n)
    length = len(n)
    
    for i in range(length-2, -1, -1):
        
        if int(li[i]) > int(li[i+1]):
            
            if li[i] != "0":
                li[i] = str(int(li[i]) - 1)
                for k in range(i+1,length):
                    li[k] = "9"
            else:
                temp = i - 1
                while li[temp] == "0":
                    temp -= 1
                li[temp] = str(int(li[temp]) - 1)
                for k in range(temp+1,length):
                    li[k] = "9"
                
    ans = ""
    for m in li:
        ans += m
        
    ans = str(int(ans))
    g.write("Case #"+ str(j)+ ": "+ ans +'\n')
        
            
    
    