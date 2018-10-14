
n = int(input());
tidy = False;
number = 0;
for i in range(n):
    x = int(input());
    for j in range(x,-1,-1):
        tidy = False;
        #print(j);
        k = str(j);
        number = int(k[0]);
        for l in range(len(k)):
            #print(k[l])
            if(int(k[l])<number):
                break;
            elif(l+1==len(k)):
                tidy = True;
                print("Case #"+str(i+1)+": "+str(j));
            number = int(k[l]);
        if(tidy==True):
            break;
        
                
                
        
