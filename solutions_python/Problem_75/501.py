import sys

def main():
    infile = open('B-large.in', 'r');
    cases = int(infile.readline());
    f = open('B-large.out', 'w')

    bases = ['QWERASDF']  
    
    for case in range(1, cases+1):
        ans = 0
        line = infile.readline().strip().split();
        #print line
        
        C = int(line[0])
        transforms = {}
        for c in range(C):
            t = line[1+c]
            transforms[t[0:2]] = t[2]
            transforms[t[::-1][1:]] = t[2]
        
        #print transforms
        
        opposites = {}
        D = int(line[1+C])
        for d in range(D):
            o = line[2+C+d]
            if not o[0] in opposites:
                opposites[o[0]] = []
            opposites[o[0]].append(o[1])
            if not o[1] in opposites:
                opposites[o[1]] = []
            opposites[o[1]].append(o[0])
        #print opposites
        
        N = int(line[2+C+D])
        string = line[3+C+D]
        
        l = ''
        for s in string:
            l += s
            if l[-2:] in transforms.keys():
                l = l[:-2] + transforms[l[-2:]]
                #print l[:-2], transforms[l[-1:]]
            elif l[-1] in opposites.keys():
                if any(e in l[:-1] for e in opposites[l[-1]]):
                    l = ''
        
        #print l
        
        """
        idx = 0
        while True:
            
            if idx >= len(string):
                break
            if idx <= 0:
                idx += 1
                continue
            el = string[idx]
            #print string, el
            try:
                if idx <= 0:
                    raise Exception
                s = string[idx-1]
                t = transforms[el+s]
                
                string = string[:idx-1] + t + string[idx+1:]
                
                #print "changed!"
                #print string
                idx += 1
                continue
            except:
                pass
            if el in opposites.keys():
                if any(e in string[:idx] for e in opposites[el]):
                    #print "opposites?", string[:idx-1], el, opposites[el]
                    string = string[idx+1:]
                    idx = 0
            idx += 1
        if l != string:
            print "WTF!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", string, l
        """
        ans = [s for s in l]
        ans = '[' + ', '.join(ans) + ']'
        s = "Case #%d: %s\n" % (case, ans)
        print s,
        f.write(s)
    
    f.close()
main();