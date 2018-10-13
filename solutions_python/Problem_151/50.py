class Node:
	def __init__(self, chr):
		self.chr = chr
		self.children = {}

	def add_child(self, s):
		if s == "":
			return
		if s[0] in self.children:
			self.children[s[0]].add_child(s[1:])
		else:
			child = Node(s[0])
			child.add_child(s[1:])
			self.children[s[0]] = child

	def num_nodes(self):
		ans = 1
		for c in self.children:
			ans += self.children[c].num_nodes()
		return ans

class Trie:
	def __init__(self):
		self.root = Node("$")

	def add(self, s):
		self.root.add_child(s)

	def count(self):
		a = self.root.num_nodes()
		if a == 1:
			return 0
		return a

def assign(upto, strs, ans, servers):
	if upto == len(strs):
		tries = [Trie(), Trie(), Trie(), Trie()][:len(servers)]
		for i in xrange(len(servers)):
			for s in servers[i]:
				tries[i].root.add_child(s)
		ans_ = 0
		for i in tries:
			ans_ += i.count()
		if ans_ in ans:
			ans[ans_] += 1
		else:
			ans[ans_] = 1
		return
	for i in xrange(len(servers)):
		servers[i].append(strs[upto])
		assign(upto+1, strs, ans, servers)
		servers[i].pop()

def f():
	m, n = map(int, raw_input().split())
	strs = []
	for i in xrange(m):
		strs.append(raw_input())
	servers = [[], [], [], []][:n]
	ans = {}
	assign(0, strs, ans, servers)
	best = 0
	y = 0
	for i in ans:
		if i >= best:
			best = i
			y = ans[best]
	return "%s %s" % (best % 1000000007, y)

T = input()
for i in xrange(1, T+1):
	print "Case #%s: %s" % (i, f())

