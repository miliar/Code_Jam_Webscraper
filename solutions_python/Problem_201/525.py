import sys
import queue

def main():
	T = int(input())

	for t in range(1, T+1):
		n,k = map(int, input().split())

		tab = {}
		pos = 1

		tab[n] = 1
		Q = queue.Queue()
		Q.put(n)
		ansL = ansR = 0

		while Q.empty() == False:
			size = Q.get()
			nodeL = nodeR = (size-1)//2
			if (size-1)&1: nodeL+=1

			if pos+tab[size]-1 >= k:
				ansL = nodeL
				ansR = nodeR
				break

			pos += tab[size]

			if nodeL not in tab:
				Q.put(nodeL)
				tab[nodeL] = tab[size]
			else:
				tab[nodeL] += tab[size]

			if nodeR not in tab:
				Q.put(nodeR)
				tab[nodeR] = tab[size]
			else:
				tab[nodeR] += tab[size]



		print ("Case #" + str(t) + ": " + str(ansL) + " " + str(ansR))

if __name__ == "__main__":
	main()