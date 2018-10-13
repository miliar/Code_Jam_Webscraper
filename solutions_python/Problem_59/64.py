import sys

tcases=int(raw_input())

class Node(object):
	

	def __init__(self,nm):
		self.name=nm
		self.children={}
	
	def add_child(self,node):
		self.children[node.name]=node


def add_path(node,path):
	if(len(path)==0):
		return 0
		
	if(path[0] in node.children):
		return add_path(node.children[path[0]],path[1:len(path)])		
	else:
		node.children[path[0]]=Node(path[0]);
		return 1+add_path(node.children[path[0]],path[1:len(path)])		

for tcase in range(tcases):
	inp=[int(t) for t in raw_input().split()]
	n=inp[0];
	m=inp[1];
	#print n,m
	
	existing=[]
	
	root=Node('');
	
	for i in range(n):
		#print raw_input().split('/')
		path=(raw_input().split('/'));
		path=path[1:len(path)]
		add_path(root,path)
	
	new=[]
	cnt=0;
	for i in range(m):
		path=(raw_input().split('/'));
		path=path[1:len(path)]
		#print path,cnt
		cnt+=add_path(root,path)
		#print cnt
	
	sys.stdout.write('Case #%d: %d\n'%(tcase+1,cnt))
	
		
	

	
	
