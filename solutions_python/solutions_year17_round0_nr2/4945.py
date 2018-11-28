def is_tidy(list_x):
    while list_x != []:
        min_list = min(list_x)
        if list_x.index(min_list) == 0:
            list_x.remove(min_list)
        else:
            return False
    return True
    

fc_r = open(r"C:\Users\PANDYASH\Downloads\B-small-attempt0.in","r")
fc_w = open("output_B_small","w")
t=int(fc_r.readline())

for i in range(1,t+1):
    n = int(fc_r.readline())
    for x in range(n,0,-1):
        x_str = str(x)
        list_x = list(x_str)
#         print(list_x,min(list_x))
        if (is_tidy(list_x)):
            fc_w.write("case #"+str(i)+": "+str(x)+"\n")
            break
        
fc_w.close()
fc_r.close()        