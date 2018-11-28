'''A bunch of work that I am done with

class node():
    def __init__(self, value, parent):
        self.parent=parent
        self.value=value
        self.left=None
        self.right=None
        self.walk=[self]
        self.value_walk=[self.value]
        self.current_walk=True
        self.current_value_walk=True
        self.factor=0
    
    def balance(self, node):
        #update the balance factor
        if node is self.left:
            self.factor-=1
        if node is self.right:
            self.factor+=1
        if self.factor<-1:
            pass
        if self.factor>1:
            pass
    
    def invalidate_walk(self):
        self.current_walk=False
        self.current_value_walk=False
        if self.parent:
            self.parent.invalidate_walk()
    
    def set_left(self, n):
        self.left=n
        self.invalidate_walk()
        self.balance(n)
        #self.delta_factor=-1
    
    def set_right(self, n):
        self.right=n
        self.invalidate_walk()
        self.balance(n)
        #self.delta_factor=1
    
    def search(self, value):
        if value==self.value:
            return self
        if value>self.value:
            if self.right is None:
                return False
            return self.right.search(value)
        if value<self.value:
            if self.left is None:
                return False
            return self.left.search(value)
    
    def inorder_walk(self):
        if self.current_walk:
            return self.walk
        nodes=list()
        if self.left is not None:
            nodes[len(nodes):]=self.left.inorder_walk()
        nodes.append(self)
        if self.right is not None:
            nodes[len(nodes):]=self.right.inorder_walk()
        self.walk=nodes
        self.current_walk=True
        return nodes
    
    def inorder_value_walk(self):
        if self.current_value_walk:
            return self.value_walk
        nodes=list()
        if self.left is not None:
            nodes[len(nodes):]=self.left.inorder_value_walk()
        nodes.append(self.value)
        if self.right is not None:
            nodes[len(nodes):]=self.right.inorder_value_walk()
        self.value_walk=nodes
        self.current_value_walk=True
        return nodes
    
    def preorder_walk(self):
        nodes=list()
        nodes.append(self)
        if self.left is not None:
            nodes[len(nodes):]=self.left.preorder_walk()
        if self.right is not None:
            nodes[len(nodes):]=self.right.preorder_walk()
        return nodes
    
    def __str__(self):
        return 'node: '+str(self.value)
    
    def __repr__(self):
        return 'node: '+str(self.value)
    
    #I made this, but I do not believe that I need it
    def predecessor(self):
        if self.left is None:
            parent=self.parent
            current=self
            while current is not parent.right:
                    current=parent
                    parent=parent.parent
        else:
            n=self.left
            while n.right is not None:
                n=n.right
            return n

class tree_set():
    def __init__(self, *args):
        self.is_empty=True
        self.root=None
        for arg in args:
            self.add(arg)
    
    def add(self, arg):
        grandparent=None
        parent=self.root
        left=False
        while parent is not None:
            grandparent=parent
            if parent.value>arg:
                parent=parent.left
                left=True
            else:
                parent=parent.right
                left=False
        if grandparent is None:
            self.root=node(arg,None)
        else:
            n=node(arg, grandparent)
            if left:
                assert grandparent.left is None
                grandparent.set_left(n)
            else:
                assert grandparent.right is None
                grandparent.set_right(n)
    
    def search(self, value):
        return self.root.search(value)
    
    def inorder_walk(self):
        return self.root.inorder_walk()
    
    def inorder_value_walk(self):
        return self.root.inorder_value_walk()
'''
def prior(vals, val):
    x=prior_index(vals, val)
    if x is not None:
        return vals[x]
    return None

def prior_index(vals, val):
    left=0
    right=len(vals)
    index=(left+right)//2
    while left<right-1:
        if val==vals[index]:
            return val
        elif val<vals[index]:
            right=index
        else:
            left=index
        #print(sequence[index], left, right)
        index=(left+right)//2
    if val<vals[left]:
        return None
    return left

def after(vals, val):
    x=after_index(vals, val)
    if x is not None:
        return vals[x]
    return None

def after_index(vals, val):
    left=0
    right=len(vals)
    index=(left+right)//2
    while left<right-1:
        if val==vals[index]:
            return val
        elif val<vals[index]:
            right=index
        else:
            left=index
        #print(sequence[index], left, right)
        index=(left+right)//2
    if val<=vals[left]:
        return left
    if left+1==len(vals):
        return None
    return left+1

#test=tree_set(10,0,20,5,15)
#print(after(test.inorder_value_walk(), 20))


from sys import stdin as cin
cases=int(cin.readline())

from blist import sortedlist

for case in range(1, cases+1):
    #minS=0
    #maxS=0
    line=cin.readline().split()
    stalls=int(line[0])
    people=int(line[1])
    walk=sortedlist([0, stalls+1])
    for person in range(people):
        location=-1
        locMin=-1
        locMax=-1
        for i in range(len(walk)-1):
            test=(walk[i]+walk[i+1])//2
            if test==walk[i]:
                continue
            a=test-walk[i]-1
            b=walk[i+1]-test-1
            testMin=min(a,b)
            testMax=max(a,b)
            if testMin>locMin or (testMin==locMin and testMax>locMax):
                location=test
                locMin=testMin
                locMax=testMax 
        walk.add(location)
        
    print('Case #'+str(case)+':', locMax, locMin)