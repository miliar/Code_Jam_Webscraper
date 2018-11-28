# coding=latin-1 

if __name__ == '__main__':
    
    n = int(raw_input())
    
    for k in range(1,n+1):
        count = 0
        myline = raw_input()
        numbers = myline.split()
        ndancer = int(numbers[0])
        nsurprising = int(numbers[1])
        max = int(numbers[2])
        
        for voto in numbers[3:]:
            voto = int(voto)
            
            remaining = voto-max
            if voto == 0 and max == 0:
                count += 1
            elif voto > 0 and remaining >= ((max-1)*2):
                count +=1
            elif voto > 0 and (remaining >= ((max-2)*2)) and nsurprising > 0:
                count += 1
                nsurprising -= 1
        print "Case #"+str(k)+": "+str(count)
        
        
    
    
    