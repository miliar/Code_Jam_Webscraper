print "\n".join([(lambda x: "Case #"+str(c+1)+": "+["OFF","ON"][x[1]%(2**x[0])==(2**x[0]-1)] )(map(int,raw_input().split())) for c in xrange(int(raw_input()))])
