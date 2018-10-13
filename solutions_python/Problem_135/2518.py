from sys import argv
script, ipfile = argv

 
def compare(C,D):

    cnt = 0
    val = 0
    
    for i in range(0,4):
        for j in range(0,4):
            
            if C[i] == D[j]:
                cnt = cnt + 1
                val = C[i]
        

    return val, cnt


ip = open(ipfile,'r')

readip = ip.read()
readip = readip.split('\n')

A = []
for i in range(0,4):
    A.append([0,0,0,0])

B = []
for i in range(0,4):
    B.append([0,0,0,0])


C = [0,0,0,0]
D = [0,0,0,0]



i = 1
j = 0

while (j < int(readip[0])):
 
    
    get_row_no1 = int(readip[i]) - 1
    
    i = i+1

    for k in range(0,4):

        get_row = readip[i]
        get_row = get_row.split()
                
        for l in range(0,4):
            A[k][l] = int(get_row[l])
            
        i = i+1
    

    for k in range(0,4):
        C[k]= A[get_row_no1][k]
        
    get_row_no2 = int(readip[i]) - 1
    
    i = i+1

    for k in range(0,4):

        get_row = readip[i]
        get_row = get_row.split()

        for l in range(0,4):
            B[k][l] = int(get_row[l])

        i = i+1



    for k in range(0,4):
        D[k]= B[get_row_no2][k]


    val, T = compare(C,D)

    if (T == 0):
        print "Case #%d: Volunteer cheated!" %(j+1)

    elif (T > 1):
        print "Case #%d: Bad magician!"%(j+1)

    else:
        print "Case #%d: %d"%(j+1, val)

    j = j+1
    
ip.close

