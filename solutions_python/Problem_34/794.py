import re
import sys


class TestCase:
    def __init__(self,exp,number):
        exp=exp.replace("(","[")
        exp=exp.replace(")","]")
        self.reg = re.compile(exp)
        self.name = "Case #%d" % number
        self.count = 0
    
    def test(self,patterns):
        for pattern in patterns:
            if self.reg.match(pattern) is not None:
                self.count +=1

    def __str__(self):
        return "%s: %d" % (self.name , self.count)


def main():
    if len(sys.argv)>1:
        test_cases=[]
        test_patterns=[]
        f = open(sys.argv[1],"r")
        if f:
            line= f.readline().split(' ')
            valL=int(line[0])
            valD=int(line[1])
            valN=int(line[2])
            for i in range(valD):
                test_patterns.append( f.readline() )
            
            #start test
            for i in range(valN):
                test_cases.append( TestCase(f.readline(),i+1) )
            #start test
            for case in test_cases:
                case.test(test_patterns)
                print case
        else:
            print "Couldnt load file"
    else:
        print "give test filename"
if __name__=='__main__':
    main()