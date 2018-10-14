import sys

file=open(sys.argv[1])
lines=file.readlines()
file.close()

primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]

N=int(lines[0])
count=1
for i in range(0,N):
    splits=0
    S=int(lines[count])
    count=count+1
    names={}
    for j in range(0,S):
        names[lines[count].rstrip()]=primes[j]
        count=count+1
    Q=int(lines[count])
    count=count+1
    product=1
    for k in range(0,Q):
        query=lines[count].rstrip()
        product *= names[query]
        tcount=0
        for m in names.keys():
            if product%names[m]==0:
                tcount+=1
        if tcount==len(names):
            splits+=1
            product=names[query]
        count=count+1
    print 'Case #'+str(i+1)+': '+str(splits)
