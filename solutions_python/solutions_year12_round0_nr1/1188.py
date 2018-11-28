
def main():
	n = int(raw_input())
	g={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','z':'q','q':'z'}
	'''print(g.values)'''
	for j in range(n):
		s1 = raw_input()
		s2=[0]*len(s1)
		for i in range(len(s1)):
			s2[i] = g[s1[i]]
		print("Case #" + str(j+1) + ": " +''.join(map(str,s2)))
		n-=1

if __name__=='__main__':
	main()
