import math

f_in = open("C-small-attempt0.in","r")
f_out = open("C-small-attempt0.out","w")

data = f_in.readlines()
f_in.close()

num_cases = int(data.pop(0))


def fair(n):
    s = str(n)
    ok = True
    for p in range(len(s)):
        if s[p]!=s[-p-1]:
            ok = False
    return ok
    

for i in range(num_cases):
    #print ("////////////////////////")

    line =  (data.pop(0).split()) 
    start =  int(line[0])
    stop =  int(line[1])+1
    #print(">", math.floor(math.sqrt(start)), math.ceil(math.sqrt(stop) ))

    c=0
    for n in range(math.floor(math.sqrt(start)),math.ceil(math.sqrt(stop))):
        if(n*n>=start and n<stop):
            if (fair(n)):
                if(fair(n*n)):
    #                print("  ",n,n*n)
                    c+=1
        #print (n)
    #print(c)        
    

    
    output= "Case #{0}: {1}".format(str(i+1),c)
    print(output)
    f_out.write(output+'\n')
   
f_out.close()    

                

print('done')
