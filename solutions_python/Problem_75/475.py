


def solve(pb):
	nb_switch = int(pb[0])
	switch = dict()
	for i in xrange(1,nb_switch+1,1):
		if pb[i][0] not in switch:
			switch[pb[i][0]]=[]
		if pb[i][1] not in switch:
			switch[pb[i][1]]=[]

		switch[pb[i][0]].append((pb[i][1], pb[i][2]))
		switch[pb[i][1]].append((pb[i][0], pb[i][2]))

	nb_clear = int(pb[nb_switch+1])
	clear = dict()
	for i in xrange(nb_switch+2,nb_clear+nb_switch+2,1):
		if pb[i][0] not in clear:
			clear[pb[i][0]]=[]
		if pb[i][1] not in clear:
			clear[pb[i][1]]=[]

		clear[pb[i][0]].append(pb[i][1])
		clear[pb[i][1]].append(pb[i][0])
	size = int(pb[nb_switch+nb_clear+2])
	string = pb[nb_switch+nb_clear+3]

	result = []
	for i in xrange(size):
		done=0
		if string[i] in switch:
			if len(result)>0:
				last = result.pop()
				for a,b in switch[string[i]]:
					if last == a:
						result.append(b)
						done = 1
						break
				if done == 0:
					result.append(last)
		if string[i] in clear and done == 0:
			for search in clear[string[i]]:
				if done==1:
					break
				for letter in result:
					if letter==search:
						result=[]
						done = 1
						break
		
		if done==0 :
			result.append(string[i])

	return result

def clean(res):
	t= '['
	w=1
	for i in res:
		if i != '*':
			if w==1:
				w=0
			else:
				t+=', '
			t+= i
	t+= ']'
	return t

if __name__ == '__main__':
	n = int(raw_input())
	b = [[_ for _ in raw_input().split()] for i in xrange(n)]
	for i in xrange(n):
		print 'Case #'+str(i+1)+': '+clean(solve(b[i]))


