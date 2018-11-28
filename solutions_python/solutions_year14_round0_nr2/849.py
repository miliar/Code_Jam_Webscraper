file=open("input.in","r")
file2 = open('output.out', 'w')

def write(output):
    print(output)
    file2.write(output+"\n")

def should_buy(C,F,X,f):
    return ( C/f+X/(f+F)) < X/f

test_cases = int(file.readline())
for i in range(test_cases):
    args = file.readline().strip().split()
    
    C = float(args[0])
    F = float(args[1])
    X = float(args[2])
    total_time = 0
    rate = 2
    
    if(X<C):
        write("Case #"+str(i+1)+": "+str(X/2))
    else:
        while(True):
            if(should_buy(C,F,X,rate)):
                total_time += C/rate
                rate += F
            else:
                total_time += X/rate
                break
        write("Case #"+str(i+1)+": "+str(total_time))
        
file.close()
file2.close()
print("Done")            
        
        
        




 
