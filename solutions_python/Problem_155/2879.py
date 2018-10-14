#!/usr/bin/python3

f = open('A-large.in', 'r')
fw = open('solutionA2.txt', 'w')
testcase_count = int(f.readline().strip()) # dont really need the count 

for (test_case_number, line) in enumerate(f):

    addcounter = 0
    totalcounter = 0

    s = line.strip().split()
    
    groupcount = int(s[0])
    data = s[1]
    
    
    for (shyness, amount) in enumerate(data):
        amount = int(amount)
        
        # are there enough people to make the next group stand up?
        if totalcounter < shyness and amount != 0:
            # add as many people as needed to make totalcounter = shyness
            addcounter += shyness - totalcounter
            totalcounter = shyness + amount
        else:
            # there are enough people. add the new standups
            totalcounter += amount

    fw.write("Case #{}: {}\n".format(test_case_number+1, addcounter))
    # print("Case #{}: {}".format(test_case_number+1, addcounter))

f.close()
fw.close()
    
