#Google Code Jam Qualification Round 2016
#Problem A. Counting Sheep

in_file = open('A-small-attempt2.in',"r")
out_file = open('A-small-attempt2.out', "w")

N = int(in_file.readline())
for i in range(1,N+1):
    a = in_file.readline().split()
    k = int(a[1])
    data = [(i=='+') for i in a[0]]
    length = len(data)
    
    count = 0
    for j in range(length-k+1):
        if not(data[j]):
            count += 1
            for jj in range(k):
                data[j+jj] = not(data[j+jj])
    right = True
    for j in range(length-k+1,length):
        if not(data[j]):
            out_file.write("Case #"+str(i)+": "+"IMPOSSIBLE"+"\n")
            right = False
            break
    if right:   out_file.write("Case #"+str(i)+": "+str(count)+"\n")
        
    
in_file.close()
out_file.close()