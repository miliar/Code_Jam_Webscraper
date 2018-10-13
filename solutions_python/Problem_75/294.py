import sys, os

class Magicka(object):
    
    def __init__(self, line):
        words = line.split(" ")
        joinrules = int(words[0])
        self.joinrules = {}
        for i in range(joinrules):
            block = words[i + 1]
            a, b, c = block
            self.joinrules[a + b] = c
            # also apply the inversion
            self.joinrules[b + a] = c
        destroy_index = joinrules + 1
        destroyrules = int(words[destroy_index])
        self.destroyrules = []
        for i in range(destroyrules):
            self.destroyrules.append(words[i + 1 + destroy_index])
        self.test_string = words[-1]
    
    def apply_joins(self, string):
        # because our only operations are a substitution at the end
        # or a new character, we only have to look at the last item
        if len(string) > 1:
            last = string[-2:]
            if last in self.joinrules:
                # not sure if the recursion is necessary, but it should
                # never hurt
                string = self.apply_joins(string.replace(last, self.joinrules[last]))
        return string
        
    def apply_destruction(self, string):
        for pair in self.destroyrules:
            if pair[0] in string and pair[1] in string:
                return ""
        return string
    
    def apply_rules(self, string):
        string = self.apply_joins(string)
        return self.apply_destruction(string)
            
    def solve(self):
        current_string= ""
        for i in range(len(self.test_string)):
            current_string = "%s%s" % (current_string, self.test_string[i])
            #print "testing %s" % current_string
            current_string = self.apply_rules(current_string)
            #print "got back %s" % current_string
        return current_string.strip()
            

    def __str__(self):
        return "join rules: %s\ndestroy rules: %s\ntest string: %s" % \
                    (" ".join("%s:%s" % (k,v) for k, v in self.joinrules.items()),
                     " ".join(str(m) for m in self.destroyrules),
                     self.test_string)
    
        
    
        
        
def solve(filename):
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(fname) as data:
        first = True
        case = 1
        for line in data:
            if first:
                games = int(line)
                first = False
            else:
                game = Magicka(line)
                def list_format(string):
                    return "[%s]" % ", ".join(string)
                print "Case #%s: %s" % (case, list_format(game.solve()))
                case += 1
                
    

if __name__ == "__main__":
    solve("B-large.in")