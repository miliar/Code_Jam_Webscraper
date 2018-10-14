import sys

def check(s):
	for i in range(1, len(s)):
		if int(s[i-1]) > int(s[i]):
			return False
	return True

def stupid(k):
	mj = 0
	for j in range(k+1):
		if check(str(j)):
			mj = j
	return mj

def clever(k):
	sk = list(str(k))
	if check(sk):
		return k
	mj = 0
	for i in range(len(sk)):
		t = map(int, sk[:])
		if t[i] > 0:
			t[i] -= 1
			for j in range(i+1,len(sk)):
				t[j] = 9
			asstr = ''.join(map(str, t))
			asint = int(asstr, 10)
			if check(asstr) and mj <= asint:
				mj = asint
	return mj


t = int(sys.stdin.readline())
for i in range(t):
	k = int(sys.stdin.readline())
	mj = clever(k)
	print('Case #%d: %d' % (i+1, mj))
