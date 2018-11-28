def main():
    fi = open('A-small-attempt2.in')
    #fi = open('probelm-a.in')
    fo = open('A-small-attempt2.out', 'w')
    t = int(fi.readline())
    
    for i in range(t):
        tc = fi.readline().split()
        p, pd, pg = int(tc[0]), int(tc[1]), int(tc[2])
        
        o = 'Broken'
        d = 1
        gw = 0
        gp = float(p)
        gw = float(p)
        
        if (pd >= 0 and pd < 100):
            if pg < 100:
                o = 'Possible'
            else:
                o = 'Broken'
        
        if (pd == 100):
            if (pg <= 100 and pg > 0):
                o = 'Possible'
            else:
                o = 'Broken'
                
        if pd > 0 and pg == 0:
            o = 'Broken'
        
        if o != 'Broken':
            while(True):
                gwp = float(gw/gp) * 100
                #print gw, gp, gwp
                
                if gwp == pd:
                    break
                
                if gw == 0:
                    gp = gp -1
                    gw = gp -1
                else:
                    gw = gw -1
                    
                if gp == 0:
                    break
                    
        if gp == 0:
            o = 'Broken'    
    
        
        fo.write("Case #%d: %s\n" % (i+1, o))
        print "Case #%d: %s" % (i+1, o)        

if __name__ == "__main__":
    main()