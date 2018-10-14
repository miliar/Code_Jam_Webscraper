# -*- coding: utf-8 -*-
import sys

N = 4

if __name__ == '__main__':
	T = int(input())
	for t in range(T):
		hint1 = int(input())-1
		board1 = []
		for j in range(N):
			board1.append([int(i)-1 for i in sys.stdin.readline().split()])
		hint2 = int(input())-1
		board2 = []
		for j in range(N):
			board2.append([int(i)-1 for i in sys.stdin.readline().split()])
		print(board1,file=sys.stderr)
		print(board2,file=sys.stderr)
		
		options = [0]*N*N;
		for i in range(N):
			options[board1[hint1][i]] += 1
			options[board2[hint2][i]] += 1
		print(options,file=sys.stderr)
		
		candidates = []
		for n in range(len(options)):
			if options[n]==2:
				candidates.append(n)
		print(candidates,file=sys.stderr)
		
		ans = 0
		if len(candidates)==0:
			ans = 'Volunteer cheated!'
		elif len(candidates)>=2:
			ans = 'Bad magician!'
		else:
			ans = candidates[0]+1
		print('Case #{}: {}'.format(t+1,ans))
		print('Case #{}: {}'.format(t+1,ans),file=sys.stderr)
