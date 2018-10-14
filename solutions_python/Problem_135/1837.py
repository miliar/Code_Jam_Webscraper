
infile = open('/home/suguman/Downloads/A-small-attempt0.in','r')
outfile = open('/home/suguman/Desktop/output1.txt','w')

x = int(infile.readline())

for i in range(x):
    num1 =int(infile.readline())
    for k in range(4):
        if k == num1-1:
            row1  = (infile.readline()).split()
            
        else:
            bleh = (infile.readline())

    num2 =int(infile.readline())
    for k in range(4):
        if k == num2-1:
            row2  = (infile.readline()).split()
            
        else:
            bleh = (infile.readline())
    len_ans = 0
    for j in range(4):
        for k in range(4):
            if (row1[j] == row2[k]):
                ans = row1[j]
                len_ans  = len_ans + 1
                

    if len_ans == 0:
        outfile.write('Case #'+str(i+1)+': ' + 'Volunteer cheated!'+'\n')
    elif len_ans == 1:
        outfile.write('Case #'+str(i+1)+': ' + ans+'\n')
    else:
        outfile.write('Case #'+str(i+1)+': ' + 'Bad magician!'+'\n')


    

            
        
    
