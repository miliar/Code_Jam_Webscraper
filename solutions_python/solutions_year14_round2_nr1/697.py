#! /usr/bin/python3

from sys import stdin

def nomulti(word):
	r = [[word[0],1]]
	for lettre in word[1:]:
		if r[-1][0] != lettre:
			r.append([lettre,1])
		else:
			r[-1][1] += 1
	return r

def homogen(words):
	# check fegla
	noms = [nomulti(w) for w in words]
	if len(set([''.join([i[0] for i in nom]) for nom in noms])) != 1:
		return 'Fegla Won'

	vectors = [[n[index][1] for n in noms] for index in range(len(noms[0])) ]
	#print('We got : \n{}'.format('\n'.join('{}'.format(i) for i in noms)))
	#print(vectors)

	resultat = 0
	for v in vectors:
		moy = sum(v)//len(v)
		resultat += sum([abs(x-moy) for x in v])


	return resultat




if __name__ == '__main__':
	
	T = int(stdin.readline())

	res = []
	for i in range(T):

		N = int(stdin.readline())
		words = []
		for j in range(N):
			words.append(stdin.readline().strip())

		res.append(homogen(words))

	print('\n'.join(['Case #{:d}: {}'.format(x+1,res[x]) for x in range(len(res))]))