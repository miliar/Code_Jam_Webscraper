import math
def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())

def NOD(a, b):
    while b:
        a,b = b, a%b
    return a

def gen_primes(max):
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(max+1) if primes[x]]

def is_prime(N):
    i = 3
    if not(N % 2):
        return 0
    while i*i < N:
        if not(N % i):
            return 0
        i += 3
    return 1

case_number = readint()
for case in xrange(case_number):
    N, P = readlinearray()
    if P > 2**N - 1:
        must, may = 2**N - 1, 2**N - 1
    else:
        #print(N, P)
        must = 0
        while 2**N - 2**(N-math.floor(math.log(must+1, 2))) < P:
            must += 1
        must -= 1
        may = 2**N - 1
        #while (2**(N - math.floor(math.log(2**N - may, 2))) - 1) >= P:
            #may -= 1
        while True:
            k = math.floor(math.log(2**N - may, 2))
            place = 2**(N - k) - 1
            if place >= P:
                may -= 1
            else:
                break
    print "Case #%s: %d %d" % (case + 1, must, may)
