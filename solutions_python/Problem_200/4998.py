import sys

with open(sys.argv[1], 'r') as my_file:
    n = my_file.read()

output =  open("tidy_output.txt", 'w')

    
file = n.split("\n")
total = int(file[0])

for t in range (1,total+1):
    for i in range (int(file[t]),0,-1):
        s_digit = [int(d) for d in str(i)]
        #print (s_digit)
        sorted = True
        for d in range (0,len(s_digit)-1):
            if s_digit[d] > s_digit[d+1]:
                sorted = False
                break
        
        if sorted:
            output.write("Case #{}: {}\n".format(t,i))
            #exit
            break
 