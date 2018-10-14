import sys

def do(foo):
    f = open(foo)
    o = open(sys.argv[2],'w')
    cases = int(f.next().strip())
    for case in range(cases):
        engiens = int(f.next().strip())
        e = {}
        for x in range(engiens):
            e[f.next().strip()] = 0
        searches = int(f.next().strip())
        s = []
        for x in range(searches):
            s.append(f.next().strip())
        searched = 0
        switches = 0
        for search in s:
            if e[search] == 0:
                searched += 1
                if searched == len(e):
                    switches += 1
                    searched = 1
                    for en in e.keys():
                        e[en] = 0
            e[search] = 1
            
        o.write('Case #'+str(case+1)+': '+str(switches)+'\n')


if __name__ == '__main__':
    do(sys.argv[1])
