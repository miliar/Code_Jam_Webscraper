
class g1():
    tdict = {}
    def main(self):
        file = open("A-small-attempt0.in")
        cnt = file.readline();
        it = 1
        while 1:
            line = file.readline()
            if (not line or line[0] == '\n'):
                break
            line=line.rstrip()
            #print(line)
            l_out = ''
            
            for l in line:
                l_out = l_out + self.translate(l)
                #print self.translate(l)
                
            print 'Case #' + str(it) + ': ' + l_out
            it = it + 1

        if it != int(cnt)+1:
            print "fail"
        
            
    
    
    def translate(self, letter):
        
        self.tdict['y'] = 'a'
        self.tdict['n'] = 'b'
        self.tdict['f'] = 'c'
        self.tdict['i'] = 'd'
        self.tdict['c'] = 'e'
        self.tdict['w'] = 'f'
        self.tdict['l'] = 'g'
        self.tdict['b'] = 'h'
        self.tdict['k'] = 'i'
        self.tdict['u'] = 'j'
        self.tdict['o'] = 'k'
        self.tdict['m'] = 'l'
        self.tdict['x'] = 'm'
        self.tdict['s'] = 'n'
        self.tdict['e'] = 'o'
        self.tdict['v'] = 'p'
        self.tdict['z'] = 'q'
        self.tdict['p'] = 'r'
        self.tdict['d'] = 's'
        self.tdict['r'] = 't'
        self.tdict['j'] = 'u'
        self.tdict['g'] = 'v'
        self.tdict['t'] = 'w'
        self.tdict['h'] = 'x'
        self.tdict['a'] = 'y'
        self.tdict['q'] = 'z'
        self.tdict[' '] = ' '
        self.tdict['\n'] = '\n'
        #print self.tdict
        return self.tdict[letter]
        
g = g1()