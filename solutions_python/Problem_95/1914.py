'''
Created on 14.04.2012

@author: Andreas Bayer, GreatCombinator
'''

import os.path

class LanguageMapping(object):
    def __init__(self):
        self.__mapping = {}
        self.buildMapping()
        
    def buildMapping(self):
        self.__mapping[' '] = ' '
        self.__unused=[]
        idx=97
        while idx<123:
            self.__mapping[chr(idx)] = None
            self.__unused.append(chr(idx))
            idx += 1
        print self.__unused
        self.__mapping['y'] = 'a'
        del self.__unused[self.__unused.index('a')]
        self.__mapping['e'] = 'o'
        del self.__unused[self.__unused.index('o')]
        self.__mapping['q'] = 'z'
        del self.__unused[self.__unused.index('z')]
        
        self.buildMappingFromSentence('ejp mysljylc kd kxveddknmc re jsicpdrysi',
                                      'our language is impossible to understand')
        self.buildMappingFromSentence('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                                      'there are twenty six factorial possibilities')
        self.buildMappingFromSentence('de kr kd eoya kw aej tysr re ujdr lkgc jv',
                                      'so it is okay if you want to just give up')
        print self.__unused
        if len(self.__unused) == 1:
            for m in self.__mapping:
                if self.__mapping[m] == None:
                    self.__mapping[m] = self.__unused[0]
        for m in self.__mapping:
            print m, '-->', self.__mapping[m]
        
    
    def buildMappingFromSentence(self, sentence, mappedSentence):
        idx = 0
        while idx<len(sentence):
            self.__mapping[sentence[idx]] = mappedSentence[idx]
            if mappedSentence[idx] in self.__unused:
                del self.__unused[self.__unused.index(mappedSentence[idx])]
            idx+=1

    def getMappedChar(self, char):
        pass
    
    def getOriginalChar(self, char):
        pass
    
    def translateWord(self, word):
        pass
    
    def translateSentence(self, sentence):
        translated = ''
        idx=0
        while idx<len(sentence):
            translated += self.__mapping[sentence[idx]]
            idx+=1
        
        return translated

class GoogleRese(object):
    def __init__(self, iPath, oPath):
        self.iPath = iPath
        self.oPath = oPath
        self.translator = LanguageMapping()
        self.nrOfTestCases = 0
        self.testCases = []
        
    def read(self):
        f = open(self.iPath, 'r')
        lines = f.readlines()
        self.nrOfTestCases = int(lines[0])
        self.testCases = lines
        f.close()
    
    def write(self):
        f = open(self.oPath, 'w')
        tc = 1
        while tc < self.nrOfTestCases:
            translated = self.translator.translateSentence(self.testCases[tc].strip())
            f.write('Case #%s: %s\n' % (tc, translated))
            print 'Case #%s: %s' % (tc, translated)
            tc += 1
        translated = self.translator.translateSentence(self.testCases[tc].strip())
        f.write('Case #%s: %s' % (tc, translated))
        print 'Case #%s: %s' % (tc, translated)
        f.close()

if __name__ == '__main__':
    iPath = os.path.join('.', 'A-small-attempt2.in')
    oPath = os.path.join('.', 'A-small-attempt2.out')
    googlerese = GoogleRese(iPath, oPath)
    googlerese.read()
    googlerese.write()
    
'''def test():
    lm = LanguageMapping()
    print lm.translateSentence('ejp mysljylc kd kxveddknmc re jsicpdrysi')
    print lm.translateSentence('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
    print lm.translateSentence('de kr kd eoya kw aej tysr re ujdr lkgc jv')
    print lm.translateSentence('y qee')
    pass'''

#test()