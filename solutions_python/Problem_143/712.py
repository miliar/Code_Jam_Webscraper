I = [line.strip().split(' ') for line in open('B-small-attempt0.in')]
output = open('out.txt', 'w') # Output File
for i in range(1,int(I[0][0])+1):
    count=0
    for x in range(int(I[i][0])):
        for y in range(int(I[i][1])):
            if x&y<int(I[i][2]): count+=1;
    output.write('Case #'+str(i)+': '+str(count)+'\n')
output.close()
    
