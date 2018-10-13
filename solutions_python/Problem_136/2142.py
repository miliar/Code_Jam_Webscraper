f = open('B-large.in','r')
n = int(f.readline())
for i in range(n):
    cook_p_s = 2
    list = f.readline().split()
    C = float(list[0])
    F = float(list[1])
    X = float(list[2])
    
    if(X<C):
        out = X/cook_p_s
    elif(X>C):
        out_c2 = 0
        out_x = X/cook_p_s
        out_c = C/cook_p_s
        out = C/cook_p_s
        while(out_x > ((X/(cook_p_s+F))+out_c)):
            cook_p_s += F
            out_x = X/(cook_p_s)
            out_c = C/cook_p_s
            out += C/(cook_p_s)
        
        out = out - out_c + out_x
        out = round(out,7)
    print('Case #'+str(i+1)+': '+str(out))
