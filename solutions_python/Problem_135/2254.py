no_of_tests = int(raw_input())
for i in range(1, no_of_tests + 1):
    #first get 1st cordinate
    row1 = int(raw_input())
    j = 1
    while(j <= 4):
        
        read = raw_input()
        if (j == row1):
            options1 = (read.rsplit(" "))
        j = j + 1
    row2 = int(raw_input())
    j = 1
    while(j <= 4):
        
        read = raw_input()
        if (j == row2):
            options2 = (read.rsplit(" "))
        j = j + 1
    soln = 0
    count = 0
    for item in options1:
        if item in options2:
            soln = item
            count = count + 1
    #print options1
    #print options2
    if count == 1:
        print "Case #" + str(i) + ":" + " " + str(soln)
    elif count == 0:
        print "Case #" + str(i) + ":" + " " + str("Volunteer cheated!")
    else:
        print "Case #" + str(i) + ":" + " " + str("Bad magician!")
    
                
                       
                       
    
            
