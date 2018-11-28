import pickle,string

table=pickle.load(open('translater'))

n=int(raw_input())

for i in xrange(1,n+1):
    print 'Case #{}: {}'.format(i,string.translate(raw_input(),table))
