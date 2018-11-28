fin = open('A-small-attempt0.in','r')
lines = fin.readlines()
fin.close()

fout = open('A.out','w')

t = int(lines[0])
for i in range(0,t):
    answer1 = int(lines[i*10 + 1])
    arrange1 = lines[i*10+answer1 + 1].strip()
    answer2 = int(lines[i*10+5 + 1])
    arrange2 = lines[i*10+ 5 + answer2 + 1].strip()
    numbers1 = arrange1.split(' ')
    numbers2 = arrange2.split(' ')
    output = []
    for j in range(0,len(numbers1)):
        for r in range(0,len(numbers2)):
            if(numbers1[j]==numbers2[r]):
                output.append(numbers1[j])
    if(len(output)==1):
        fout.write('Case #%s: %s\n'%(i+1,output[0]))
    elif(len(output)>1):
        fout.write('Case #%s: Bad magician!\n'%(i+1))
    elif(len(output)==0):
        fout.write('Case #%s: Volunteer cheated!\n'%(i+1))

fout.close()
        
