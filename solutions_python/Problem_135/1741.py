import sys

lines = [line.strip() for line in open('input.txt')]

testCase = lines[0]
testCase = int(testCase)

if testCase < 1 or testCase > 100:
    print("Test case not in range")
    sys.exit()

for x in range(0, int(testCase)):
    curStart = (x * 10) + 1
    output = "Bad magician!"
    
    s1 = lines[curStart]
    s1 = int(s1)
    s2 = lines[curStart + 5]
    s2 = int(s2)

    if s1 < 1 or s1 > 4 or s2 < 1 or s2 > 4:
        print("Submit not in range")
        sys.exit()

    t1 = []
    for i in range(1, 5):
        t1.append(lines[i + curStart].split())

    t2 = []
    for y in range(6, 10):
        t2.append(lines[y + curStart].split())
        #print(y + curStart)

    #check which card
    foundCount = 0        
    for z in t1[s1 - 1]:
        for y in t2[s2 - 1]:
            #print("checking if y: " + str(y) + " = z: " + str(z))
            if z == y:
                output = z
                foundCount = foundCount + 1

    if foundCount > 1:
        output = "Bad magician!"

    #test cheat
    found = 'f';
    for z in t1[s1 - 1]:
        for y in t2[s2 - 1]:
            if z == y:
                found = 't';

    if found == 'f':
        output = "Volunteer cheated!"
            

    #print(str(s1) + " " + str(s2))
    print("Case #" + str(x + 1) + ": " + output)
