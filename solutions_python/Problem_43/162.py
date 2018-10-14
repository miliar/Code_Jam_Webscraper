def clean(s):
    if s[len(s)-1:]=='\n':
        return s[0:len(s)-1]
    else:
        return s

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])

class AYB:

    def __init__(self,argv):
        self.argv = argv
        self.cases = 0
        self.case = 0
        self.res = {}
        self.input()
        
    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close()
        self.cases = int(self.lines[0])
        self.lines = self.lines[1:]
        
    def output(self):
        s = ''
        for h, k in self.res.iteritems():
            s += 'Case #%s: %s\n' % (h, k)                
        sys.stdout.write(s)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(s)
        f.close()

    def step(self):
        self.word = clean(self.lines[0])
        self.lines = self.lines[1:]
        self.value = {}
        self.dict = '1'
        self.value[self.word[0]] = '1'
        self.where = 0
        for i in range(1,len(self.word)):
            try:
                t = self.value[self.word[i]]
                self.dict += self.value[self.word[i]]                    
            except:
                if self.where == 1:
                    self.value[self.word[i]] = str(2)
                    self.where = 3
                elif self.where < 10:
                    self.value[self.word[i]] = str(self.where)
                    self.where += 1                
                else:
                    self.value[self.word[i]] = chr(self.where-10+97)
                    self.where += 1
                self.dict += self.value[self.word[i]]
        if len(self.value) == 1:
            self.n = int(self.dict,len(self.value)+1)
        else:
            self.n = int(self.dict,len(self.value))
        self.case += 1
        self.res[self.case] = self.n

    def Run(self):
        for i in range(1,self.cases+1):
            self.res[i] = 0
            self.step()
        self.output()
    

if __name__ == "__main__":
    import sys
    print int('111111111',2)
    ayb = AYB(sys.argv[1])
    ayb.Run()
