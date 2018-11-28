n=int(input())
for i in range(n):
    item_int=int(input())
    item_str=str(item_int)
    temp_list=list(item_str)
    var=False
    for j in range(len(temp_list)-1):
        if(temp_list[j]>temp_list[j+1]):
            var=True
            break
    while(var):
        item_int-=1
        item_str=str(item_int)
        temp_list=list(item_str)
        flag=0
        for j in range(len(temp_list)-1):
            if(temp_list[j]>temp_list[j+1]):
                var=True
                flag=1
                break
        if(flag==0):
            var=False
    print("Case #"+str(i+1)+":", item_int)
            
