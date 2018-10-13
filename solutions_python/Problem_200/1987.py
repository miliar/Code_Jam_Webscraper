#Google Code Jam Qualification Round 2016
#Problem A. Counting Sheep


in_file = open('B-small-attempt4.in',"r")
out_file = open('B-small-attempt4.out', "w")

N = int(in_file.readline())
for i in range(1,N+1):
    data = [int(x) for x in in_file.readline().split()[0]]
    length = len(data)
    
    ans = 0
    count = 0
    for j in range(length-1):
        if data[j] > data[j+1]:
            data[j] -= 1
            for k in range(j+1,length):
                data[k] = 9
            for k in range(j,0,-1):
                if data[k] < data[k-1]:
                    data[k] = 9
                    data[k-1] -= 1
                    break
            break
    out_file.write("Case #"+str(i)+": "+str(int(''.join(map(str,data))))+"\n")
        
        
    
in_file.close()
out_file.close()