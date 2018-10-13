testcases = int(raw_input())
t=1

while t <= testcases:
    num_of_integers = int(raw_input())
    
    numbers = raw_input()
    templist = numbers.split()
    number_list_1 =[]
    for num in templist:
        number_list_1.append(int(num))
        
    numbers = raw_input()
    templist = numbers.split()
    number_list_2 =[]
    for num in templist:
        number_list_2.append(int(num))
        
    number_list_1.sort()
    number_list_2.sort()
    number_list_2.reverse()
    
    i=0
    total = 0
    while i < num_of_integers:
        total = total + number_list_1[i] * number_list_2[i]
        i += 1
    
    print "Case #%d: %d" % (t, total)
    
    t += 1
