import math

file_strings = []
with open("oversized_pancake_flipper.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())

T = file_strings[0] # number of testcases
file_strings.pop(0)

for i in range(1, int(T) + 1):
	# setting up S and K
	flag = True
	flips = 0
	S, K = file_strings.pop(0).split()[0:2]
	K = int(K)		
				
	if K % 2 == 0: # if K is even we have another case for impossible
		# if the number of - is odd it is impossible
		sum = 0
		for k in range(len(S)):
			if S[k] == '-':
				sum += 1
		if sum % 2 != 0:
			flag = False
	
	if flag != False:
		final_neg = len(S) - 1 #Initially we suppose the final neg is the last character in S. Index of last - sign
		while(final_neg >= K - 1):
			if(S[final_neg] == '+'): # if it's a + we move on
				final_neg -= 1
				continue
			else: # we flip it
				for ind in range(final_neg - K + 1, final_neg + 1): # flipping the characters
					if S[ind] == '+':
						S = S[:ind] + '-' + S[ind + 1:]
					else:
						S = S[:ind] + '+' + S[ind + 1:]
				flips += 1 # count the flip
				final_neg -=1
		for chars in range(K):
			if S[chars] == '-':
				flag = False
				break

	if flag == False:
		print("Case #{}: IMPOSSIBLE".format(i))
	else:
		print("Case #{}: {}".format(i, flips))