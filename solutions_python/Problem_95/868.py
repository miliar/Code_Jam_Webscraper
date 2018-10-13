'''
Created on 06/05/2011

@author: German
'''
import string

if __name__ == '__main__':
    g2t = {}
    g2t['y'] = 'a'
    g2t['e'] = 'o'
    g2t['q'] = 'z'
    g2t[' '] = ' '
    g2t['\n'] = '\n'
    
    g = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv'
    t = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup'
    
    assert len(g) == len(t)
    
    for l_g, l_t in zip(g,t):
        if l_g in g2t:
            assert g2t[l_g] == l_t
        else:
            g2t[l_g] = l_t
    missing = [x for x in string.lowercase if x not in g2t.values()]
    g2t['z'] = missing[0]
    for l in string.lowercase:
        assert l in g2t
    
    

    with open('sol.out', 'w') as out:
        with open('A-small-attempt0.in', 'r') as f:
            T = int(f.readline())
            for i in xrange(1,T+1):
                case = f.readline().strip()
                    
                res_str = "Case #%d: %s\n" % (i, ''.join(map(g2t.__getitem__, case)))
                print res_str,
                out.write(res_str)
            
            
            
            