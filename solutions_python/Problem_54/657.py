import sys

def gcd(x,y):
    while x:
        x, y = y % x, x
    return y

linect = 0
testcases = []
firstentries = []
with open("input.txt", 'r') as inp:
    for line in inp:
            token = line.split()
            linect +=1
            if linect == 1:
                testno = int(token[0])
                continue
            eventct = int(token.pop(0))
            firstentries.append(int(token[0]))
            testcases.append(list(set([(int(token[(i+ 1) % eventct]) - int(token[(i)]))for i in range(eventct)])))
                       
if linect -1 != testno:
    print ("No. of test cases do not match the number given in the file. Exiting...")
    sys.exit(1)    


            
with open("output.txt", 'w') as out:
    for test_idx in  range(testno):
        curr_gcd = testcases[test_idx][0]
        for event_idx in range(len(testcases[test_idx]) - 1):
            curr_gcd = gcd(curr_gcd,testcases[test_idx][event_idx + 1])
        curr_gcd = abs(curr_gcd)     
        result = (curr_gcd - (firstentries[test_idx] % curr_gcd)) % curr_gcd
            
        outstring = "Case #" + str(test_idx + 1) + ": " + str(result) + "\n"
        out.write(outstring)
        
print ("Everything Done!")    
sys.exit()    
                    