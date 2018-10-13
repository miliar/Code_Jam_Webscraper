'''
Created on 8 avr. 2017

@author: franc
'''
from builtins import range

class TidyNumber(object):
    '''
    classdocs
    '''
    number = []


    def __init__(self, string):
        '''
        Constructor
        '''
        self.number = []
        for c in string :
            self.number.append(int(c))
        print(self.number)
        
    def isTidy(self):
        print ("Test tidy " + str(self.number))
        if len(self.number)== 1:
            return -1;
        for x in range(len(self.number)-1):
            if (self.number[x]>self.number[x+1]):
                return x
        return -1
            
    def fromString(self, string):
        self.number = []
        for c in string :
            self.number.append(int(c))
        print(self.number)
        
    def nextTidy(self):
        lastTidyIndex = self.isTidy()
        while(lastTidyIndex >= 0):
            MSBs = str(int(self.toString(self.number[:lastTidyIndex+1]))-1)
            LSBs = ""
            for x in range((lastTidyIndex + 1),len(self.number)):
                LSBs += "9"
            print("num"+ str(self.number) + "msb: " + MSBs + " lsb "+ LSBs)
            self.fromString( MSBs + LSBs)
            lastTidyIndex = self.isTidy()
        return True
    
    def toString(self,strNum):
        out = ""
        start = True
        for c in strNum:
            if(start and c==0):
                pass
            else:
                start = False
                out += str(c)
        return  out