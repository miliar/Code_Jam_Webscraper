fr = open('input.txt' , 'r')
fw = open('output' , 'w')



test_cases = int(fr.readline())

for i in xrange(1,test_cases+1):
    
    raggio, liters = fr.readline().split()
    
    raggio = int(raggio)
    liters = int(liters)


    sum = 0
    
    starting_area = 0
    area = 0
    
    count = -1

    while(sum <= liters):
        
        
        starting_area = raggio * raggio

        area = (raggio +1) * (raggio +1) - starting_area

        sum += area

        raggio +=2
        count +=1


    fw.write("Case #%d: %d\n" %(i , count))

        
