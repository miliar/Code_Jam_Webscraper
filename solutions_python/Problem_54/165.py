# the function to calculate the GCD
def gcd(a,b):
	"""gcd(a,b) returns the greatest common divisor of the integers a and b."""
	if a == 0:
		return b
	return abs(gcd(b % a, a))

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

input = open('2.in', 'r')
output = open('2.out', 'w')
n = int(input.readline())
for i in range(1,n+1):
    ti = [int(x) for x in input.readline().split(' ')]
    ti = ti[1:]
    m = min(ti)
    d = reduce(gcd, [t - m for t in ti])
    # print (d, m, d-gcd(m,d))
    answer = (-m) % d
    # print [(t+answer) % d for t in ti]
    output.write("Case #%d: %d\n" % (i, answer))


#   if 0 == (K+1) % pow(2,N):
#       print "%d %d ON" % (N,K)
#       output.write('Case #' + str(i) + ": ON\n")
#   else:
#       print "%d %d OFF" % (N,K)
#       output.write('Case #' + str(i) + ": OFF\n")

