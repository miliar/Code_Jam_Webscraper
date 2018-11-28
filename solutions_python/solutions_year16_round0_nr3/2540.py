from random import randrange
import random
import time

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

def primes(n):
    #Borrowed from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def probably_prime(n, k):
    # From http://stackoverflow.com/questions/14613304/rabin-miller-strong-pseudoprime-test-implementation-wont-work
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def do_stuff(b):
	factors = []
	for base in xrange(2,11):
		x = int(b, base)
		if not probably_prime(x, 50):
			timeout = time.time() + 10
			for i in xrange(2, int(x**0.5) + 1):
				if time.time() > timeout:
					return []
				div, mod = divmod(x, i)
				if mod == 0:
					# print "{0} (Base {1}) - FACTOR: {2}".format(x, base, i)
					factors.append(i)
					break
		else:
			# print str(b) + " possibly prime in base " + str(base)
			return []
	return factors

small_primes = primes(2**22)

T = int(raw_input().strip())

#Get input
nj = raw_input().split(" ")
for case in xrange(T):
	print "Case #{}:".format(case+1)
	N = int(nj[0].strip())
	J = int(nj[1].strip())

	coinCount = 0
	coins = []

	while coinCount < J:
		r = random.randrange(2**(N-1), 2**N-1)
		if r % 2 == 0:
			r += 1
		b = "{0:b}".format(r)

		res = do_stuff(b)
		if res and b not in coins:
			print str(b) + " " + " ".join(str(x) for x in res)
			coins.append(b)
			coinCount += 1
