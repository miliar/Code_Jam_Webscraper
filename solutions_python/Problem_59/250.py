import collections, re,sys,os



class preftree:
    id=0
    parent=None
    tree = None
    leaves = None
    id_data_map=None
    #for gcj
    new_ent=0 
    create_phase=False
    def __init__(self):
        self.tree = {}
        self.id=0
        self.id_data_map ={}
        self.parent = {}
        self.leaves = []

        self.new_ent=0 
        self.create_phase=False
        
    def insert(self,word):
        #insert new word, and update 'parent' alongwith
        curr = self.tree
        p=0
        word_len = len(word)
        for i in  range(word_len):
            l = word[i]
            found = False
            for tmp_l, tmp_id in curr.keys():
                if(l==tmp_l):
                    found = True                     
                    curr = curr[(tmp_l,tmp_id)]
                    p = tmp_id
            
            if(not found):
                
                self.id+=1
                if(self.create_phase):self.new_ent+=1
                self.id_data_map[self.id] = l
                curr[(l,self.id)] = {}
                curr = curr[(l,self.id)]
                self.parent[self.id]=p
                if(i == word_len-1):self.leaves.append(self.id)
                #try:
                #    self.leaves.remove(p)
                #except:pass
                p=self.id

    def set_create(self):
        self.create_phase=True

        



    def print_entries(self):
        '''print all words in the prefix tree'''
        for leaf in self.leaves:
            arr=[]
            self.append_parent(arr, leaf)
            print "".join(map(lambda(x):self.id_data_map[x], arr))
        


    def append_parent(self, arr,node_id):
        '''helper function for print_entries'''
        if(node_id==0): return
        else:
            arr.insert(0,node_id)
            self.append_parent( arr, self.parent[node_id])


    
    def is_member(self, word, idx=0, t=None):
        '''Checks whether word is a member of the prefix tree.
        If not, also returns (in addition to the match status - True/ False)
        the first index from the left in the given word that failed to match.'''
        if(not t): t = self.tree
        if(len(t)==0 ):
            if(idx >= len(word)): return False, idx-1
            #else: return False, idx-1 
       
        for d,node_id in t:
            
            #d= self.id_data_map[k]
            if(word[idx] == d):
                if(idx==len(word)-1 ): 
                    if(node_id in self.leaves): return True, node_id
                    else: return False,idx
                return self.is_member(word, idx+1, t[(d,node_id)])
        return False,idx


    def delete(self, word):
        '''delete word from prefix tree
        currently implemented by deleting entry from leaves - not very space efficient'''
        res = self.is_member(word)
        if(not res[0]):
            print "Word not a member of prefix tree."
        else:
            self.leaves.remove(res[1])
        



class node:
    data = None
    children = None
    def __init__(self, data=None):
        if(not data): self.data = data
        children = []



       

def newtree():
    '''creates a new and empty prefix tree'''
    return node()


def insert(preftree, word):
    '''adds word to the prefix tree'''
    curr_node =preftree
    for i in range(len(word)):
        l = word[i]
        found = False
        if(l not in map(lambda(x):x.data,curr_node.children)): 
            curr_node.children.append(node(l))
        curr_node = curr[l]
    
                
        



def delete(preftree, word):
    ''' deletes word from the prefix tree '''




def is_member(preftree, word):
    '''Checks whether word is a member of the prefix tree.
    If not, also returns (in addition to the match status - True/ False)
    the first index from the left in the given word that failed to match.'''




def print_tree(preftree):
    '''prints given prefix tree'''
    












def readfile():
    f=open(sys.argv[1])
    lineno=0
    meta = True
    limit=0
    case=0
    n,m=0,0
    all_files=[]
    for line in f:
        lineno+=1
        if(lineno==1):continue
        line=line.strip()
        if(meta):
            case+=1
            n,m = line.split(" ")
            n,m=int(n), int(m)
            limit = lineno+n+m
            meta=False
            all_files = []
        else:
            temp = line.split("/")
            temp[0]='*'
            all_files.append(temp)
        
            if(lineno==limit):
                meta=True
                p=preftree()
                for i in all_files[:n]:
                    p.insert(i)
                p.set_create()
                for i in all_files[n:]:
                    p.insert(i)
                if(n==0):
                    print "Case #%d: %d"%(case,p.new_ent-1)
                else:
                    print "Case #%d: %d"%(case,p.new_ent)
readfile()
