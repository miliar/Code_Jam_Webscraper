def standing():
    
    inpfile= open("Ainput.txt", "r")
    outfile= open("Aoutput.txt", "w")
    tests= int(inpfile.readline())
    for test in range(tests):
        a, b= [int(i) for i in inpfile.readline().split()]
        b= str(b)
        #print(b)
        b= [int(i) for i in b]
        #print(b, a)
        if len(b)!= a+1:
            for s in range(a+1- len(b)):
                b.insert(0, 0)
        #print(b)
        
        stand= 0
        get= 0
        for i in range(a+1):
            if i-stand> 0:
                if b[i]> 0:
                    add= i-stand
                else:
                    add= 0
            else:
                add= 0
            #print(i, add, a+1, "iadd")
            get+= add
            stand+= b[i]+ add
            #print(get, stand, "gs")
        
        z= "Case #"+ str(test+ 1)+ ": "+ str(get)
        print(z)
        outfile.write(z)
        outfile.write("\n")
    return

standing()