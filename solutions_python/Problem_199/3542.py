my_file = open('/Volumes/Almacenamiento/PE/CodeJam2017-1A/A-large.in','r')
my_out = open('/Volumes/Almacenamiento/PE/CodeJam2017-1A/20171A.out','w')

T = int(my_file.next())

for i in range(T):
    (string, K) = [x for x in my_file.next().split()]
    K = int (K)
    
    
    flips = 0
    index = 0
    while '-' in string:
        index = string.index('-')
        if index + K > len(string):
            flips = 'IMPOSSIBLE'
            break
        for j in range(K):
            if string[index+j] == '-':
                string = string[:(index+j)] + '+' + string[(index+j+1):]
                #string[K+j].replace('-','+')
            else:
                #string[K+j].replace('+','-')
                string = string[:(index+j)] + '-' + string[(index+j+1):]
        flips = flips +1
        try:
            if string.index('-')<index or flips>len(string):
                flips = 'IMPOSSIBLE'
                break
        except ValueError:
            break
        #ahora hacia el otro lado
        
        index = string.rfind('-')
        if index - K < 0:
            flips = 'IMPOSSIBLE'
            break
        for j in range(K):
            if string[index-j] == '-':
                #string[K-j].replace('-','+')
                string = string[:(index-j)] + '+' + string[(index-j+1):]
            else:
                #string[K-j].replace('+','-')
                string = string[:(index-j)] + '-' + string[(index-j+1):]
        flips = flips +1
        try:
            if string.rfind('-')>index or flips>len(string):
                flips = 'IMPOSSIBLE'
                break
        except ValueError:
            break
        
    my_out.write('Case #'+str(i+1)+': '+str(flips)+'\n')
    print 'Case #'+str(i+1)+': '+str(flips)+'\n'
        

my_file.close()
my_out.close()