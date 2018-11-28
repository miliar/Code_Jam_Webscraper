for t in xrange(int(raw_input())):raw_input();candy=map( int, raw_input().split() );print"Case #%d: %s"%(t+1,"NO"if reduce(lambda x,y:x^y,candy,0) else str(sum(candy)-min(candy)))
