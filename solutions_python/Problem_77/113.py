#For a permutation which is a cycle of length n, recursively compute the expected sorting time. Do this by computing the expected contribution of each element e. This is the sum from 1 to n of the probability e is in a cycle of length i (this is 1/n) times the expected sorting time of that cycle times 1/i (since the contribution is the same for every element in the cycle). Then use linearity of expectation. Add 1 for the first shuffle.
expval=[0.0,0.0]
for n in xrange(2,101):
    #expval[n]=1+n*sum((1/n)*expval[i]*(1/i) for i in xrange(1,n+1))
    #((n-1)/n)*expval[n]=1+n*sum((1/n)*expval[i]*(1/i) for i in xrange(1,n))
    expval.append((1+sum(expval[i]/i for i in xrange(1,n)))*n/(n-1))
print expval

#And then realise that it is possible to prove by induction that expval[n]=n for n>1
