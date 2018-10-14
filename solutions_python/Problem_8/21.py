#!/usr/bin/env python

import sys

# return list of prime numbers
def primes(start, N):
    prime=[True for p in range(N+1)]
    prime[0]=False
    prime[1]=False
    p=1
    while p+p<=N:
	# find next known prime number
	while not prime[p]:
	    p+=1
	    if p>N: break
	if p>N: break
	# eliminate multiples of p
	i=p+p
	while i<=N:
	    prime[i]=False
	    i+=p
	p+=1
    return [p for p in range(start,N+1) if prime[p]]

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    A, B, P = map(int, inputfile.readline().strip().split(" "))
    sys.stderr.write("case %d: A=%d B=%d P=%d\n" % (case, A, B, P))
    # setindex[i-A]=s if i belongs to set s
    setindex=[i-A for i in range(A,B+1)]
    # sets[s]=[i-A: i belongs to set s]
    sets=[[i-A] for i in range(A,B+1)]
    for p in primes(P, B/2):
	#sys.stderr.write("p=%d\n" % p)
	# find first multiple of p in [A,B]
	i=A/p*p
	if i<A: i+=p
	if i>B: continue
	# number of set to which i belongs
	t=setindex[i-A]
	# move all multiples of p to set t, and also all number in the same
	# sets as multiples of p
	i+=p
	while i<=B:
	    #sys.stderr.write("i=%d\n" % i)
	    # set to which i belongs
	    s=setindex[i-A]
	    if s!=t:
		# move all elements in s to t
		for j in sets[s]:
		    setindex[j]=t
		    sets[t].append(j)
	    i+=p
    numsets=len(set(setindex))
    print "Case #%d: %d" % (case, numsets)
