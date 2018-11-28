
class MagickaGame(object):
    def __init__(self, rules):
        input = rules.split()
        combineCount = int(input[0])
        opposeCount = int(input[combineCount+1])
        self.combine = input[1:combineCount+1]
        self.oppose = input[combineCount+2: combineCount + opposeCount + 2]

        self.tester = input.pop()
        #print rules.strip()

    def run(self, debug=False):

        if debug:
            print "rules:%s" % (self.combine)
            print "rules:%s" % (self.oppose)

        elem = []
        chars = {}
        for char in self.tester:
            chars.setdefault(char,0)
            chars[char]+=1
            elem.insert(0, char)
            if debug: 
                print elem, chars
            combined = False
            if len(elem)>1:
                for rules in self.combine:
                    if ((elem[0] == rules[0] and elem[1] == rules[1])or
                        (elem[0] == rules[1] and elem[1] == rules[0])):
                        #replace first two chars with replacement
                        chars[elem.pop(0)]-=1
                        chars[elem[0]]-=1
                        chars.setdefault(rules[2],0)
                        chars[rules[2]]+=1
                        elem[0] = rules[2]
                        combined = True

                        if debug:
                            print "%s%s->%s - %s" % (rules[0], rules[1], rules[2], list(elem))

                        
            if not combined:
                for rules in self.oppose:
                    if ((rules[1]==char and chars.get(rules[0],0))or
                        (rules[0]==char and chars.get(rules[1],0))):
                        if debug:
                            print "%s - %s -> ''" % (rules, list(elem))
                        elem = []
                        chars = {}
        if debug:
            print list(elem)
        elem.reverse()
        return str(elem).replace("'","")

if __name__=="__main__":
    import sys
    #MagickaGame("1 DEP 1 WE 10 FSEEDWESFF").run(True)
    #sys.exit()
    for case in range(int(sys.stdin.readline())):
        game = MagickaGame(sys.stdin.readline())
        print "Case #%d: %s" % (case+1, game.run())
        
        
