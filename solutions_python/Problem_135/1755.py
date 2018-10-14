def func(list1,list2,r1,r2):
    count=0
    for i in list1[r1-1]:
        if(i in list2[r2-1]):
            count=count+1
            ans=i
    if(count==0):
        return 'Volunteer cheated!'
    elif(count>1):
        return 'Bad magician!'
    else:
        return ans
file=open('A-small-attempt1.in','r')   
cases=int(file.readline())
for case in range(1,cases+1):
    r1=int(file.readline())
    
    mat11=file.readline()
    list11=mat11.split()
    mat12=file.readline()
    list12=mat12.split()
    mat13=file.readline()
    list13=mat13.split()
    mat14=file.readline()
    list14=mat14.split()

    list1=[list11,list12,list13,list14]

    r2=int(file.readline())

    mat21=file.readline()
    list21=mat21.split()
    mat22=file.readline()
    list22=mat22.split()
    mat23=file.readline()
    list23=mat23.split()
    mat24=file.readline()
    list24=mat24.split()

    list2=[list21,list22,list23,list24]     

    print('Case #'+str(case)+': '+func(list1,list2,r1,r2))
