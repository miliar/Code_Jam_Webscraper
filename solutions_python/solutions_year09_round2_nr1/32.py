import os, sys, re
fi = open("A-large.in", "r")
fo = open("a.out", "w")

REGEX1 = re.compile(r'^\(\s*([0-9\.]+)\s*\)$')
REGEX2 = re.compile(r'^\(\s*([0-9\.]+)\s+(\w+)\s+(.+)\s*\)')

class TreeNode:
	def __init__(self, prob, feat=None, leaves=None):
		self.prob = prob
		self.feat = feat
		self.leaves = leaves
	def calc(self, features):
		if self.feat:
			return prob * leaves[0 if self.feat in features else 1].calc(features)
		else:
			return prob



def get_prob(tnode):
	global feats
	if len(tnode) == 1:
		return tnode[0]
	else:
		has_feat = tnode[1] in feats
		return tnode[0] * get_prob(tnode[2] if has_feat else tnode[3])

def make_tree(txt):
	txt = txt.strip()
	#tokens = re.findall(r'([0-9\.]+|\w+|\(|\))', txt)
	#print tokens
	pycode = re.sub(r'(\)|[0-9]+\.[0-9]+)', r'\1,', re.sub(r'([a-z]+)', r'"\1",', txt)).rstrip(', ')
	tree = eval(pycode)
	return tree

def test_case(ncase):
	global feats
	nl = int(fi.readline())
	t = ''
	for i in range(nl):
		t += fi.readline().rstrip() + ' '
	tree = make_tree(t)
	print >>fo, 'Case #%d:' % ncase
	na = int(fi.readline())
	for i in range(na):
		feats = fi.readline().split()[2:]
		print >>fo, '%.7f' % get_prob(tree)

ncases = int(fi.readline())
for i in range(1, ncases+1):
	test_case(i)

fo.close()