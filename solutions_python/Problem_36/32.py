from StringIO import StringIO

def all_indices(str, chr):
    for i, cc in enumerate(str):
        if cc == chr:
            yield i

def num_substrings( line, phrase ):
    paths = [(x,1) for x in all_indices(line,phrase[0])]
    
    for c in phrase[1:]:
        nextpaths = []
        indices = list(all_indices(line, c))
        #print c, indices
        for ix in indices:
            nextpaths.append( (ix, sum([x[1] for x in paths if x[0] < ix]))  )
        paths = nextpaths
    
    return sum([x[1] for x in paths])

def getit(strm, phrase):
    N = int(strm.readline())
    
    ret = []
    for i in range(N):
        line = strm.readline().strip()
        addret = "Case #%d: %s"%(i+1,str(num_substrings( line, phrase )).rjust(4, "0")[-4:])
        print addret
        ret.append( addret )
        
    return "\n".join( ret )

def main(basename, phrase):
    fp = open( basename+".in" )
    
    out = getit(fp, phrase)
    
    fpout = open( basename+".out", "w" )
    fpout.write( out )
    fpout.close

if __name__=='__main__':
    phrase = "welcome to code jam"
    main( "C-large", phrase )
    
    #bigline = """So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."""
    #print num_substrings( bigline, phrase )
