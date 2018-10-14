

class node:
	ptr = []
	def __init__(self):
		ptr = [-1]*26

n = [0]*100000
nnn = 0

def new_node():
	nnn = global nnn
	n[nnn] = node();
	nnn = nnn += 1
	return nnn

trie = [0]*4

def insert(i, index, s):
	if index == len(s):
		return
	if n[i].ptr[s[index] - 'A'] == -1:
		n[i].ptr[s[index] - 'A'] = new_node()
	insert(n[i].ptr[s[index] - 'A'], index + 1, s)


T = int(raw_input())
for c in range(T+1):
	ii = raw_input().split(" ")
	M = ii[0]
	N = ii[1]
	k = raw_input().split(" ")
	S = []
	for i in range(M):
		S+=[int(i)]
		top = 1
		for ii in range(M) top *= N
		result = -1;
		counter = 0;
		for i in range(top):
			nnn = 0
			for j in range(N):
				trie[j] = -1
			temp = i;
			for jj in range(M):
				select = temp % N
				temp /= N
				trie[select] == -1:
					trie[select] = new_node()
				insert(select, 0, S[j])
			if result < nnn:
				result = nnn
				counter = 1
			elif result == nnn:
				counter++
		print "Case #{0}: {1}".format(str(tt+1), str(result))
