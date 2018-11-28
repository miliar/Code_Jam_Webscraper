#Google Code Jam Qualification Round 2016
#Problem A. Counting Sheep

def divide(N):
    N -= 1
    if N%2 == 0:
        return [N//2, N//2]
    else:
        return [N//2, N//2 + 1]


name = 'C-large'
in_file = open(name+'.in',"r")
out_file = open(name+'.out', "w")

N = int(in_file.readline())
for i in range(1,N+1):
    print(i)
    read = in_file.readline().split()
    N = int(read[0])
    K = int(read[1])
    
    dic = {N:1}
    while K>0:
        maxkey = max(dic.keys())
        maxval = dic[maxkey]
        dic.pop(maxkey,None)
        divideN = divide(maxkey)
        for k in divideN:
            if k in dic:
                dic[k] += maxval
            else:
                dic[k] = maxval
        K -= maxval
    out_file.write("Case #"+str(i)+": "+str(divideN[1])+" "+str(divideN[0])+"\n")
   
in_file.close()
out_file.close()