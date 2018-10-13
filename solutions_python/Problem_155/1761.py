def Run_OV():
    f=open('D://A-large.in','r')
    line=f.readlines()
    i=1
    F_out=open('D://Output2.txt','w')
    while i < len(line):
        S=line[i].split(" ")[1].rstrip()
        Result=Stand_OV(S)
        F_out.write("Case #"+str(i)+": "+str(Result)+ "\n")
        i = i + 1
        print Result 
    
    F_out.close()
    

def Stand_OV(S_level):
    #S_max=input("Please Enter S Max Value")
    Friends=0
    Sum_aud=0
    for i in range(len(S_level)):
        if i>0:
            Sum_aud= Sum_aud+ eval(S_level[i-1])
            if  i > Sum_aud:
                temp_friends = i - Sum_aud
                Friends = Friends + temp_friends
                Sum_aud=Sum_aud + temp_friends
               
    return Friends 
                    
                      
        
        
        
        
        
    
    