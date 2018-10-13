import re
import math

class TreeNode(object):
	Ls,Rs = -1,-1
	debug = False
	def __init__(self,spaces):
		self.left = None
		self.right = None
		self.empty_spaces = spaces
		self.max_spaces_left = -1
		self.max_spaces_right = -1

	def occupy(self):
		if TreeNode.debug:
			print('running occupy')
		self.left = TreeNode(math.floor(((self.empty_spaces-1)/2)))
		self.right = TreeNode(math.ceil(((self.empty_spaces-1)/2)))
		self.max_spaces_left = self.left.empty_spaces
		self.max_spaces_right = self.right.empty_spaces
		if TreeNode.debug:
			print(self.max_spaces_left, self.max_spaces_right)
		self.empty_spaces = -1
		TreeNode.Ls = self.max_spaces_left
		TreeNode.Rs = self.max_spaces_right
		if TreeNode.debug:
			print('Ls',TreeNode.Ls,'Rs',TreeNode.Rs)
		return max(self.max_spaces_left,self.max_spaces_right)

	def find(self):
		if TreeNode.debug:
			print('running find')
			self.print()
		# reached a leaf node
		if self.max_spaces_left < 0 and self.max_spaces_right < 0:
			if TreeNode.debug:
				print('reached a leaf node')
			return self.occupy()
		# go right
		elif self.max_spaces_left < 0 or self.max_spaces_right > self.max_spaces_left:
			if TreeNode.debug:
				print('going right')
			self.max_spaces_right = self.right.find()
			return max(self.max_spaces_left,self.max_spaces_right)
		# go left
		elif self.max_spaces_right < 0 or self.max_spaces_right <= self.max_spaces_left:
			if TreeNode.debug:
				print('going left')
			self.max_spaces_left = self.left.find()
			return max(self.max_spaces_left,self.max_spaces_right)

	def print(self):
		print(TreeNode.Ls,TreeNode.Rs,self.left,self.right,self.empty_spaces,self.max_spaces_left,self.max_spaces_right)

def run2(n,k):
	root_node = TreeNode(n)
	# print(root_node.empty_spaces)
	for i in range(k):
		# print('person',i)
		root_node.find()
		# print('run2:',TreeNode.Ls,TreeNode.Rs)

	return max(TreeNode.Ls,TreeNode.Rs),min(TreeNode.Ls,TreeNode.Rs)


def run(n,k):
	stalls = '1'+'0'*n+'1'
	# print(stalls)
	# print(matchObj.group(1))
	# for i in range(1,k+1):
	# set1 = {}
	# thres1 = 0
	# for i in range(1,k+1):
	# 	for j in range(n):
	# 		if stalls[j] ~= '0':
	# 			continue
	# 		tmp = list(stalls)
	# 		tmp[j] = '2'
	# 		tmp = ''.join(tmp)
	# 		print(tmp)
	# 		matchObj = re.search('(0*)2(0*)',tmp)
	# 		# print(matchObj.group(0))
	# 		Ls = len(matchObj.group(1))
	# 		Rs = len(matchObj.group(2))
	# 		if min(Ls,Rs) > thres1:
	# 			set1 = {}
	# 			set1[j] = [Ls,Rs]
	# 			thres1 = min(Ls,Rs)
	# 		elif min(Ls,Rs) == thres1:
	# 			set1[j] = [Ls,Rs]
	# 	if len(set1) == 1:
	# 		for k,v in set1.items():
	# 			tmp = list(stalls)
	# 			tmp[j] = '1'
	# 			stalls = ''.join(tmp)
	# 	else:
	# 		for k,v in set1.items():


	return n,k


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = input().split()
  n = int(n)
  k = int(k)
  a,b = run2(n,k)
  print("Case #{}: {} {}".format(i, a, b))
  # check out .format's specification for more formatting options

