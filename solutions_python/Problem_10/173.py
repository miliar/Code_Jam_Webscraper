#set dubug to off
DEBUG = 1

import sys

class Key:
    def __init__(self,places):
        self.places = places
        self.lettersFreq = []

    def addLetter(self,letterFreq):
        if len(self.lettersFreq) <= self.places:
            self.lettersFreq.append(letterFreq)
            return len(self.lettersFreq)
        return 0

    def getTotalPresses(self):
        result = 0
        index = 1
        for item in self.lettersFreq:
            print "item:",item,"has index:",index
            result += item * index
            index += 1
        return result

class Phone:
    def __init__(self,keys, places):
        self.keys = keys
        self.currKey = 0
        self.keyDict = {}
        for x in range(keys):
            self.keyDict[x] = Key(places)

    def addLetter(self,letterFreq):
        print "adding:",letterFreq,"To Key:",self.currKey
        if self.keyDict[self.currKey].addLetter(letterFreq):
            self.currKey += 1
            if self.currKey == self.keys:
                self.currKey = 0
        
    def getTotalPresses(self):
        result = 0
        for item in self.keyDict.values():
            result += item.getTotalPresses()
        return result

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Usage: Message.py <input file>"
        print "Trying to load default files"
        try:
            input_file = open('message-test.in')
            output_file = open('A-output.txt','w')
        except:
            print "couldn't load default filename, see usage"
            exit()
    else:
        try:
            #we asume that the first arg is the input file name
            input_file = open(sys.argv[1])
            output_file = open('A-output.txt','w')
        except:
            print "Usage: Message.py <input file>"
            print "couldn't open the specified file name"
            exit()
    
    
    count = int(input_file.readline()[:-1])
    
    
    for x in range(count):
        output_file.write("Case #" + str(x+1) +": ")

        print "Message #",x+1
        
        [P,K,L] = [int(e) for e in input_file.readline()[:-1].split(" ")]
        freq = [int(e) for e in input_file.readline()[:-1].split(" ")]
        TestPhone = Phone(K,P)

        print "P:",P
        print "K:",K
        print "L:",L
        print "freq:",freq
        
        if P*K < L:
            response = "imposible"
        else:
            freq.sort(reverse=True)
            print "freq:",freq
            for item in freq:
                print "adding:",item
                TestPhone.addLetter(item)

            response = str(TestPhone.getTotalPresses())

        output_file.write(response+"\n")

    print "output went to:",output_file.name
    
    output_file.close()
    input_file.close()
    

    
