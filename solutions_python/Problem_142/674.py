import sys
sys.stdin = open('A-small-attempt1.in', 'r')
sys.stdout = open('A.out','w')

for p in range(int(input())):
	N = int(input())
	w = '.' + input() + '.'
	ww = '.' + input() + '.'
	if len(w) > len(ww):
		w, ww = ww, w
	i, j = 0, 0
	S = 0
	while i < len(w) and j < len(ww):
		if w[i] == ww[i]:
			i += 1
			j += 1
		else:
			if i>0 and j>0 and (w[i-1] == ww[j]):
				S += 1
				ww = ww[:j-1] + ww[j:]
			elif i>0 and j>0 and (ww[j-1] == w[i]):
				S += 1
				w = w[:i-1] + w[i:]
			elif w[i] != ww[i]:
				w = ''	
		#print(w,ww)		
	if w == ww:
		print("Case #%d: %d" % (p+1, S))
	else:
		print("Case #%d: %s" % (p+1, 'Fegla Won'))