# http://snippets.dzone.com/posts/show/753
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def do(i, s):
	t = list(s)
	k = len(i)
	for x in range(len(t)):
		t[x] = s[x - x % k + i[x % k]]
	return str(t)

def calc(i, s):
	t = list(s)
	k = len(i)
	for x in range(len(t)):
		t[x] = s[x - x % k + i[x % k]]
	n = 1
	for x in range(1,len(t)):
		if(t[x] != t[x - 1]):
			n+=1
	return n

def case():
	k = int(raw_input())
	s = raw_input()
	min = 99999999
	for i in all_perms(range(k)):
		cur = calc(i, s)
		if(cur < min):
			min = cur
	print min

ncases = int(raw_input())
for i in range(ncases):
	print "Case #" + str(i+1) + ":",
	case()
