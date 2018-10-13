input_file = open('A-large.in')
output_file = open('A-large.out', 'w') 
nc =  int(input_file.readline())
for ci in range(1, nc + 1):    
    a = input_file.readline().split()
    list_string = [int(d) for d in str(a[1])]
    friend = 0
    sum = 0
    for i in range(1,int(a[0])+1):
        sum += int(list_string[i-1])
        if(sum < i and list_string[i] > 0):
            friend += (i - sum)
            sum += (i-sum)  
    output_file.write('Case #'+str(ci)+': '+str(friend)+'\n')
input_file.close()
output_file.close()        
                
                                    
                
