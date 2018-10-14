ipname = input("Enter the name of input file : ")
ip = open(ipname, "r")
o1 = "Output "
extension = ".txt"
outputname = o1 + ipname[:-3] + extension
out = open(outputname, "w")
    
# Scanning all the Test cases
T = ip.readline()
T = int(T)

# Starting the loop T times
for i in range(T):
    
    inputline = ip.readline().split()
      
    for j in range(3):
        inputline[j] = int(inputline[j])
        
    A = inputline[0]
    B = inputline[1]
    K = inputline[2]
    
    inputline = []
    
    klist = []    
    klist = list(range(K))
    
    counter = 0
    for x in range(A):
        for y in range(B):
            
            if (x & y) in klist:  
                counter += 1
            
            
       
    out.writelines("Case #%d: %d\n" % (i+1, counter))

ip.close()
out.close()