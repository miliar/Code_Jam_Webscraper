f = open('A-small-attempt2.in','r')
arr= f.readlines()
f.close()

f=open('test.out','w')
for case in range(1,int(arr[0])+1):

    row_guess_1=int(arr[(case-1)*10+1])
    arr_temp=arr[(case-1)*10+1+row_guess_1].split(" ")
    arr_row_1=set()
    for item in arr_temp:
        arr_row_1.add(int(item))
    
    row_guess_2=int(arr[(case-1)*10+6])
    arr_temp=arr[(case-1)*10+6+row_guess_2].split(" ")
    arr_row_2=set()
    for item in arr_temp:
        arr_row_2.add(int(item))
    
    inter=arr_row_1 & arr_row_2 
    if len(inter)==0:
        answer="Volunteer cheated!"
    else:
        if len(inter)>1:
            answer="Bad magician!"
        else:
            if len(inter)==1:
                for item in inter:
                    answer=str(item)
    f.write("Case #"+str(case)+": "+answer+"\n")
f.close() 


