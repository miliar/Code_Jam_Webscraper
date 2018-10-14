import itertools
import copy
import csv

def flip_item(i):
	return '-' if i == '+' else '+'

def flip(n, idx, spat):
	for i in range(0, spat):
		n[idx + i] = flip_item(n[idx + i])
	return n

def is_done(li):
	for i in li:
		if i == '-':
			return False
	return True

def find_flips(n, spat):
	if is_done(n):
		return 0
	n_flips = len(n) + 1
	n = list(n)
	perms = itertools.permutations(range(0, len(n)-(spat-1)))
	winning_perm = None
	for perm in perms:
		curr_flips = 0
		done = False
		new_n = copy.deepcopy(n)
		while done == False and curr_flips < len(perm):
			new_n = flip(new_n, perm[curr_flips], spat)
			curr_flips += 1
			done = is_done(new_n)
			if done:
				if n_flips > curr_flips:
					n_flips = curr_flips
					winning_perm = perm
	if n_flips <= len(n):
		return n_flips
	else:
		return 'IMPOSSIBLE'

inp = open('/Users/aspittel/Downloads/A-small-attempt1.in')
inp = inp.read()
inp = inp.split('\n')
write_file = open('code_jam_redo.txt', 'w+')


inp.pop(0)
inp.pop()

# with open('codejam.csv', 'wb') as csv:
# 	writer = csv.writer(csvfile)
# 	# writer.writerow(['Case', 'Spat', 'n plus', 'n minus', 'solvable', ''])
for idx, n in enumerate(inp):
	print(idx)
	write_file.write("Case #{}: {}\n".format(idx + 1, find_flips(n.split(' ')[0], int(n.split(' ')[1]))))
# 			print(n.split(' ')[0], int(n.split(' ')[1]))
# 			print(find_flips(n.split(' ')[0], int(n.split(' ')[1])))

# print(find_flips(list('+--+'), 2))