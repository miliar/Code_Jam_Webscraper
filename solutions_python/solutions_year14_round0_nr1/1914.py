fr = open('Input_small.in','r')
fw = open('Output_small.out','w')
first = []
second = []

for i in range(0, int(fr.readline())):
    count = 0
    a = int(fr.readline())
    for j in range(1, 5):
        if(j==a):
            first = fr.readline().strip('\n\t').split(" ")
        else:
            fr.readline()
            
    b = int(fr.readline())
    for k in range(1, 5):
        if(k==b):
            second = fr.readline().strip('\n\t').split(" ")
        else:
            fr.readline()
            
    for l in first:
        if l in second:
            count = count+1
            num = l

    if(count == 1):
        fw.write('Case #')
        fw.write(str(i+1))
        fw.write(': ')
        fw.write(num)
        fw.write('\n')
        
    elif(count < 1):
        fw.write('Case #')
        fw.write(str(i+1))
        fw.write(': Volunteer cheated!\n')
        
    elif(count >= 2):
        fw.write('Case #')
        fw.write(str(i+1))
        fw.write(': Bad magician!\n')
fr.close()
fw.close()
