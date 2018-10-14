'''
Created on Apr 13, 2013

@author: Osborn
'''


with open('A-small-attempt8.in') as f:
    data = f.read()
        #list = read_data.splitlines()
    list = data.splitlines()
    f.closed
    new_list1= list[1:5]
    new_list2= list[6:10]
    new_list3= list[11:15]
    new_list4= list[16:20]
    new_list5= list[21:25]
    new_list6= list[26:30]
    new_list7=list[31:35]
    new_list8=list[36:40]
    new_list9=list[41:45]
    new_list10=list[46:50]

def mysolution(input):
    x_list1=[]
    x_list2=[]
    x_list3=[]
    x_list4=[]
    y_list1=[]
    y_list2=[]
    y_list3=[]
    y_list4=[]
    
    for array_pos, array in enumerate(input):
        if array_pos==0:
            for pos, val in enumerate(array):
                if val=='X' or val=='T':
                    x_list1.append(pos)
                if val=='O' or val=='T':
                    y_list1.append(pos)
        elif array_pos==1:
            for pos, val in enumerate(array):
                if val=='X' or val=='T':
                    x_list2.append(pos)
                if val=='O' or val=='T':
                    y_list2.append(pos)
        elif array_pos==2:
            for pos, val in enumerate(array):
                if val=='X' or val=='T':
                    x_list3.append(pos)
                if val=='O' or val=='T':
                    y_list3.append(pos)
        else:
            for pos, val in enumerate(array):
                if val=='X' or val=='T':
                    x_list4.append(pos)
                if val=='O' or val=='T':
                    y_list4.append(pos)
    
    max_x=0
    for x in [x_list1,x_list2,x_list3,x_list4]:
        if len(x)>=max_x:
            max_x=len(x)
    
    max_y=0
    for y in [y_list1,y_list2,y_list3,y_list4]:
        if len(y)>=max_y:
            max_y=len(y)
                
    array_x = x_list1+x_list2+x_list3+x_list4
    array_y = y_list1+y_list2+y_list3+y_list4
    nested_listx = [x_list1,x_list2,x_list3,x_list4]
    nested_listy = [y_list1,y_list2,y_list3,y_list4]
    
    for pos, array in enumerate(nested_listx):
        if pos not in array:
            xdiag = 0
            break
        xdiag=4
    
    for pos, array in enumerate(nested_listx):
        if (3-pos) not in array:
            xdiag_ = 0
            break
        xdiag_ =4
    
    for pos, array in enumerate(nested_listy):
        if pos not in array:
            ydiag = 0
            break
        ydiag=4
        
    for pos, array in enumerate(nested_listy):
        if (3-pos) not in array:
            ydiag_ = 0
            break
        ydiag_ =4
    
    maxx_v=0
    maxy_v=0
    if array_x.count(0)>maxx_v:
        maxx_v = array_x.count(0)
    if array_x.count(1)>maxx_v:
        maxx_v = array_x.count(1)
    if array_x.count(2)>maxx_v:
        maxx_v = array_x.count(2)
    if array_x.count(3)>maxx_v:
        maxx_v = array_x.count(3)
    
    if array_y.count(0)>maxy_v:
        maxy_v = array_y.count(0)
    if array_y.count(1)>maxy_v:
        maxy_v = array_y.count(1)
    if array_y.count(2)>maxy_v:
        maxy_v = array_y.count(2)
    if array_y.count(3)>maxy_v:
        maxy_v = array_y.count(3)
        
    for array in input:
        for x in array:
            if x=='.':
                if max_x>3 and max_y>3 or maxx_v>3 and maxy_v>3 or max_x>3 and maxy_v>3 or max_y>3 and maxx_v>3:
                    return 'Game has not completed'
                if max_x<=3 and max_y<=3 and maxx_v<=3 and maxy_v<=3 and xdiag<=3 and xdiag_<=3 and ydiag<=3 and ydiag_<=3:
                    return 'Game has not completed'
                
   
    if max_x>3:
        return 'X won'
    elif ydiag>3 or ydiag_>3:
        return 'O won'
    elif xdiag>3 or xdiag_>3:
        return 'X won'
    elif max_y>3:
        return 'O won'
    elif max_x<=3 and max_y>3 or max_x<=3 and maxy_v>3 or maxx_v<=3 and max_y>3 or maxx_v<=3 and max_y>3:
        return 'O won'
    elif maxx_v>3:
        return 'X won'
    else:
        return 'Draw'


f = open('output', 'w')
f.write('Case #1: ')
f.write(mysolution(new_list1))
f.write('\n')
f.write('Case #2: ')
f.write(mysolution(new_list2))
f.write('\n')
f.write('Case #3: ')
f.write(mysolution(new_list3))
f.write('\n')
f.write('Case #4: ')
f.write(mysolution(new_list4))
f.write('\n')
f.write('Case #5: ')
f.write(mysolution(new_list5))
f.write('\n')
f.write('Case #6: ')
f.write(mysolution(new_list6))
f.write('\n')
f.write('Case #7: ')
f.write(mysolution(new_list7))
f.write('\n')
f.write('Case #8: ')
f.write(mysolution(new_list8))
f.write('\n')
f.write('Case #9: ')
f.write(mysolution(new_list9))
f.write('\n')
f.write('Case #10: ')
f.write(mysolution(new_list10))