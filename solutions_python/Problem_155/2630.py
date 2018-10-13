import random
file_name = "A-large.in"
in_file = open(file_name, "r")
ou_file = open( file_name[:-2]+"ou","w")
lines = in_file.readlines()
T = int(lines[0].rstrip("\n"))
h=1
for j in range(T):
    data = lines[h].rstrip("\n").split(" ")  
    s_max = int(data[0])    
    shyness = data[1]
    standing = 0
    additional = 0
    if s_max == 0:
        ou_file.write( "Case #"+str(j+1)+": "+str(additional)+"\n")
    else:
        for n in range(s_max+1):
            temp = int(data[1][n])
            if n == 0 and temp == 0:
                additional +=1
                standing = 1
            else:
                while standing < n:   
                    additional +=1
                    standing +=1
                standing = standing + temp
                           
        ou_file.write( "Case #"+str(j+1)+": "+str(additional)+"\n")
    h = h+1
    
    
#ou_file.write( "Case #"+str(n-w_dict)+": "+str(tot)+"\n")
ou_file.close()

