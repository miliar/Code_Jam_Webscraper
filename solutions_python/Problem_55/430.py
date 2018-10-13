import sys

linect = 0
testcases = []
testgroups = []
with open("input.txt", 'r') as inp:
    for line in inp:
            token = line.split()
            linect +=1
            if linect == 1:
                testno = int(token[0])
                continue
            if linect % 2 == 0:
                current_test = [int(token[0]), int(token[1]), int(token[2])]
                groupct = int(token[2])
                testcases.append(current_test[:])
            else:
                testgroups.append([int(token[i]) for i in range(groupct)])
                       
#if (linect -1) / 2 != testno:
#    print ("No. of test cases do not match the number given in the file. Exiting...")
#    sys.exit(1)    
            
with open("output.txt", 'w') as out:
    for test_idx in  range(testno):
        income = 0
        ridect = testcases[test_idx][0]
        capacity = testcases[test_idx][1]
        groupct = testcases[test_idx][2]
        riderct = sum(testgroups[test_idx])
        i = 0
        for ride_idx in range(ridect):
            intake = 0
            while (True):
                new_intake = intake + testgroups[test_idx][i]
                if ( new_intake> capacity)or (new_intake > riderct):
                    break
                intake = new_intake
                i = (i + 1)% groupct   
            income += intake    
            
        outstring = "Case #" + str(test_idx + 1) + ": " + str(income) + "\n"
        out.write(outstring)
        
print ("Everything Done!")    
sys.exit()    
                    