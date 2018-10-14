#!/usr/bin/python
with open('A-small-attempt0.in') as f:
    n_case = int(f.readline())
    for case in range(n_case):
        x1= 0
        x2=0
        x3=0
        x4=0
        d1=[]
        d2=[]
        first_row = int(f.readline())
        data1 = []
        data2 = []
        for i in range(4):
            data1.append(f.readline())
        row = data1[first_row-1]
        x1 = int(row.split()[0])
        x2 = int(row.split()[1])
        x3 = int(row.split()[2])
        x4 = int(row.split()[3])
        d1=[x1,x2,x3,x4]
       # print 'first row:', d1
        second_row = int(f.readline())
        for i in range(4):
            data2.append(f.readline())
        row = data2[second_row-1]
        x1 = int(row.split()[0])
        x2 = int(row.split()[1])
        x3 = int(row.split()[2])
        x4 = int(row.split()[3])
        d2 = [x1,x2,x3,x4]
        #print 'second row:',d2
        result = list(set(d1).intersection(d2))
       # print 'result is', result
        if not result:
            print 'Case #{0}:'.format(case+1), 'Volunteer cheated!'
        elif len(result) > 1:
            print 'Case #{0}:'.format(case+1), 'Bad magician!'
        else:
            print 'Case #{0}:'.format(case+1), result[0]
        
        
    
