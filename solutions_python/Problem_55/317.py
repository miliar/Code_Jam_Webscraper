import psyco
psyco.full()

def main():

    cases = int(raw_input())
    for i in xrange(0, cases):
        R, k, N = map(int, raw_input().split(" "))
        line = map(int, raw_input().split(" "))
        money=0
        for j in xrange(0, R):
            oline= list(line)
            vac=k
            while oline[0] <= vac:
                oline.pop(0)
                line.append(line.pop(0))
                vac-=line[-1]
                money+=line[-1]
                if len(oline)==0:
                    break

        print "Case #%i: %i" % (i+1, money)
    
           
main()