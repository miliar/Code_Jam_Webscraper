#! /usr/bin/pypy

import cPickle as pickle

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
values = dict( zip(map(str,range(0,10)),range(0,10)) )

def computeFingerprint(n):
    ns = map(lambda x: values[x],list(str(n)))
    first = 0
    fingerprint = []

    #find first local min, there is bound to be at least one
    for i,j in enumerate(ns):
        if j < ns[i-1]:
            first = i
            break

    l = len(ns)

    #create fingerprint for each segment starting at a local minimum
    current = primes[ns[first]]
    lastDigit = ns[first]
    position = (first+1)%l

    while not position == first:
        currentDigit = ns[position]

        if currentDigit < lastDigit: #new segment starts
            fingerprint.append(current)
            current = primes[currentDigit]
        else: #procede with old segment
            current *= primes[currentDigit]

        lastDigit = currentDigit
        position = (position+1)%l

    fingerprint.append(current)

    return fingerprint

if __name__ == "__main__":
    f = open("fingerprints.p","wb")
    
    #yes, i am paranoid about arithmetical stuff for no good reason and against
    #all rationality
    fingerprints = map(computeFingerprint,list(range((2*(10**6))+1)))
    pickle.dump(fingerprints,f)

    f.close()
