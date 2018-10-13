import itertools, sys
sys.setrecursionlimit(25000)


def find_scores_cheating(her_blocks, his_blocks):
	her_blocks = sorted(her_blocks)
	his_blocks = sorted(his_blocks)
	his_blocks.reverse()
	his_smallest_block = min(his_blocks)
	her_smallest_blocks = filter(lambda x: x<his_smallest_block, her_blocks)
	his_score = 0
	her_score = 0
	if her_smallest_blocks != []:
		his_score+=1
		his_blocks.pop(0)
		her_blocks.pop(0)
	else:
		his_blocks.sort()
		his_blocks.pop(0)
		her_blocks.pop(0)
		her_score += 1
	if her_blocks == []:
		return her_score
	else:
		return her_score + find_scores_cheating(her_blocks, his_blocks)


def find_scores_legit(her_blocks, his_blocks):
	her_blocks.sort()
	his_blocks.sort()
	her_score = 0
	his_score = 0
	print her_blocks
	print his_blocks
	for i in xrange(len(her_blocks)):
		block = her_blocks[i]
		his_bigger = filter(lambda x: x>block, his_blocks)
		if his_bigger != []:
			his_score += 1
			his_blocks.remove(min(his_bigger))
		else: 
			her_score += 1
			his_blocks.remove(min(his_blocks))
	print her_score
	return her_score

with open("D-large.in") as t:
	t = t.read().split("\n")
	with open("output", "w") as o:
		n = int(t.pop(0))
		for i in xrange(n):
			_ = t.pop(0)
			her_blocks = map(float, t.pop(0).split())
			his_blocks = map(float, t.pop(0).split())
			o.write("Case #%s: %d %d\n"%(i+1, find_scores_cheating(her_blocks, his_blocks), find_scores_legit(her_blocks, his_blocks)))

			
			












