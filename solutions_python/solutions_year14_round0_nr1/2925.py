t=int(raw_input())
for case in xrange(0,t):
    first=int(raw_input())
    card1=[]
    tmp=[]
    for i in xrange(0,4):
	tmp=map(int,raw_input().split())
	card1.append(tmp)
    second=int(raw_input())
    card2=[]
    for i in xrange(0,4):
	tmp=map(int,raw_input().split())
	card2.append(tmp)
    common=set(card1[first-1]) & set(card2[second-1])
    if len(common)==0:
	print "Case #%d: %s" % (case+1 , "Volunteer cheated!")
    else:
	el=common.pop()
	if len(common)==0:
	    print "Case #%d: %d" % (case+1 , el)
	else:
	    print "Case #%d: %s" % (case+1 , "Bad magician!")
    t-=1