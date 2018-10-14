for t in xrange(1,input()+1):(lambda(N,K):__import__("sys").stdout.write("Case #%d: %s\n"%(t,"ON"if (K&((1<<N)-1))==((1<<N)-1) else"OFF")))(map(int,raw_input().split()))
