tests = []
f = open('A-large.in', 'r')
while True:
   line = f.readline()
   if not line: break
   else: 
      tests.append(str(line).split()),
	  
f.close()

scribe = open('sample_output', 'w')
counter = ['1']
for x in tests[1:]:
        for y in x:
                minFriends = 0
                ableClappers = 0
                empty = 0
                testCnt = 0
                for m in range(len(str(y))):
                        if int(y[m]) == 0:
                                empty += 1
                                testCnt += 1
                        elif int(y[m]) > 0:
                                if testCnt <= ableClappers:
                                        ableClappers += int(y[m])
                                        testCnt += 1
                                elif testCnt > ableClappers:
                                        shortage = testCnt-ableClappers
                                        minFriends += shortage
                                        ableClappers += shortage  #add missing
                                        ableClappers += int(y[m]) #add new system
                                        testCnt += 1
                        #print minFriends


        print "Case #" + str(len(counter)) + ": " + str(minFriends) + "\n"
        scribe.write("Case #" + str(len(counter)) + ": " + str(minFriends) + "\n")
        counter.append(1)
