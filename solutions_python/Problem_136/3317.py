
def GetTime(c, f, x):
	r = 2.0
	T = x/r
	a = x/(r+f)
	t = c/r + a
	while t<T:
		T = t
		r += f
		b = x/(r+f)
		t = t - a + c/r + b
		a = b
	return T

def ReadInput():
	t = int(raw_input())
	for case in xrange(1,t+1):
		c, f, x = map(float, raw_input().split())
		print("Case #{}: {}".format(case, '{0:.7f}'.format(GetTime(c,f,x))))

if __name__ == "__main__":
	ReadInput()