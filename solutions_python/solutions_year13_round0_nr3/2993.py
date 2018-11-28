class TH:

    lines = [] 
    cases = 0 
    output = []

    def __init__(self, infile):
        fil = open(infile)
        lin = fil.readlines()
        self.cases = int(lin.pop(0).split("\n")[0])
        rmbn = lambda st: st.split('\n')[0]
        self.lines = map(rmbn,lin)


    def ans(self,ans):
        assert(len(self.output) + 1 <= self.cases)
        self.output.append(ans)

    def wo(self,outfile):
        casegen = lambda (case,ans): "Case #%d: %s" %( case+1,ans)
        fil = open(outfile,'w')
        fil.write("\n".join(map(casegen,enumerate(self.output))))
        
    
    
    
        
