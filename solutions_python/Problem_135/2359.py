with open("test.in",'r') as r:
    dataset=r.readlines()
    r.close()

test_cases=int(dataset[0][:-1])
matrix1=[]
matrix2=[]
count = 0

for i in range(0,test_cases):
    row1=int(dataset[10*i+1][:-1])
    
    matrix1.append([int(k) for k in dataset[10*i+2][:-1].split()])
    matrix1.append([int(k) for k in dataset[10*i+3][:-1].split()])
    matrix1.append([int(k) for k in dataset[10*i+4][:-1].split()])
    matrix1.append([int(k) for k in dataset[10*i+5][:-1].split()])
    row2=int(dataset[10*i+6][:-1])
    
    matrix2.append([int(k) for k in dataset[10*i+7][:-1].split()])
    matrix2.append([int(k) for k in dataset[10*i+8][:-1].split()])
    matrix2.append([int(k) for k in dataset[10*i+9][:-1].split()])
    matrix2.append([int(k) for k in dataset[10*i+10][:-1].split()])

    test1=matrix1[row1-1]
    test2=matrix2[row2-1]
    for ele1 in test1:
        for ele2 in test2:
            if ele1 == ele2:
                count += 1
                val=ele1
    if count == 1:
        print "Case #%d:" %(i+1),' ',val
    elif count >1:
        print "Case #%d:" %(i+1),' ',"Bad magician!"
    elif count ==0:
        print "Case #%d:" %(i+1),' ',"Volunteer cheated!"
    matrix1=[]
    matrix2=[]
    count=0
    

     

    
    
