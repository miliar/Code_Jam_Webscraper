from gmpy2 import mpz, isqrt, floor

data = open('a.txt', 'r').read().split('\n')

T = int(data.pop(0))

for t in range(T):
   (r,ml) = map(mpz, data.pop(0).split(' '))

   a = mpz('2')
   b = mpz(2 * r - 1)
   c = mpz(-1 * ml)
   
   ans = int(floor((isqrt(mpz(b*b - 4.0 * a * c)) - b)/(2.0 * a)))

   print 'Case #' + str(t+1) + ": " + str(ans)
