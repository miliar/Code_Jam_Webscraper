#!/bin/python
# matekm [gmail.com]

ref = "welcome to code jam"

if __name__ == "__main__":
    N = int (raw_input ())
    
    for i in range (N):
        testcase = raw_input ()
        
        counter = 0
        words = []
        for j in range (len(testcase)):
            if (testcase[j] in ref):
                if (testcase[j] == 'w'):
                    words.append(testcase[j])
                    continue
                for word in words:
                    if ((word + testcase[j]) in ref):
                        words.append (word+testcase[j])
            
        for word in words:
            if (word == ref):
                counter = counter + 1
        
        if (counter > 9999):
            counter = 9999
            
        counter = str(counter)
        counter = counter.zfill(4)
        print "Case #{0}: {1}".format (i+1, counter)
        #if (counter < 10):
        #    print "Case #{0}: 000{1}".format (i+1, counter)
        #elif (counter < 100):
        #    print "Case #{0}: 00{1}".format (i+1, counter)
        #elif (counter < 1000):
        #    print "Case #{0}: 0{1}".format (i+1, counter)
        #lif (counter < 9999):
        #    print "Case #{0}: {1}".format (i+1, counter)
        #else:
        #    print "Case #{0}: {1}".format (i+1, 9999)

        