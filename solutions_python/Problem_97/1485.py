# c_recyclednumbers.py

"""Googlers: Sorry for the swear words in my
previous submission (b_dancingwithgooglers.py)!"""

import copy

def getData(filename):
    f = open(filename, 'r')
    throwaway = f.readline()
    data = []
    for line in f:
        data.append(Set([int(a) for a in line.split()]))
    return data


class Set:
    def __init__(self, endpoints):
        self.start = endpoints[0]
        self.end = endpoints[1]
        self.count = 0
        self.pairDigits = {}
        print "about to have some tests..."
        print self.start, self.end
        print len(str(self.start)), len(str(self.end))
        for i in range(len(str(self.start)), len(str(self.end)) + 1):
            #print i
            self.pairDigits[i] = list()
        
    def checkForRecycled(self, n):
        digits = len(str(n))
        if digits <= 1:
            return None
        elif n in self.pairDigits[digits]:
            return None
        else: #let's recycle!
            found = False
            offset = 1
            while offset < digits:
                
                recycledNum = int("".join([a for a in str(n)[offset:] + str(n)[0:offset]]))
                pair = [n, recycledNum]
                pair.sort()
                
                if (len(str(recycledNum)) != digits #leading zero
                    or n == recycledNum #they're the same number
                    or pair in self.pairDigits[digits] #pair already exists
                    or recycledNum > self.end #number past end limit
                    or recycledNum < self.start): # number past start limit
                    offset += 1
                else:
                    self.pairDigits[digits].append(pair)
                    self.count += 1
                    #print "digits:", digits, "pair:", n, recycledNum, "offset:", offset
            
            return None

    def analyzeSet(self):
        for i in range(self.start, self.end + 1):
            self.checkForRecycled(i)

        print self.count
        return self.count



if __name__ == "__main__":
    filename = "c_sample.txt"
    filename = "C-small-attempt0.in"
    data = getData(filename)
    print len(data), data
    output = []

    for i in range(len(data)):
        output.append(data[i].analyzeSet())
    
    
    fout = open(filename + ".out", 'w')
    for i in range(len(output)):
        print "Case #" + str(i + 1) + ": " + str(output[i])
        fout.write("Case #" + str(i + 1) + ": " + str(output[i]) + "\n")
    fout.close()




