#!/usr/bin/python

# Google Code Jam Qualification Round C

import math

class mydict(dict):
    '''cause pythondicts are stupid, loved the perl hashes'''
    def __init__(self, default_val = 0.):
            super(mydict, self).__init__()
            self._default_val = default_val
        
    def __getitem__(self, key):
        try:
            return super(mydict, self).__getitem__(key)
        except KeyError:
            self.__setitem__(key, self._default_val)
            return self._default_val

def singleManSolver(N):
    '''returns min(Ls, Rs) and max(Ls, Rs) for the case where one person goes
    in N shower booths'''
    N = N-1
    min_val = max(0, N//2)
    max_val = max(0, int(N/2.+0.5))
    return min_val, max_val

class descTree(object):
    class treeNode(object):
        def __init__(self, N, displace, parent):
            self._parent = parent
            self._displace = displace
            self._left = None
            self._right = None
            self._best_child = None
            self._sort_vals = singleManSolver(N) + (displace,)
            #print self._sort_vals
            # self._sort_vals has:
            # min_val, max_val, displace, which are the three sorting indicies
            # placed in importance order
        
        def placePerson(self):
            # note that _sort_vals duals as N in nodes 
            # 'Places a person', i.e., splits the tree node for later search
            # then returns either child or minval and maxval
            if self.hasChild():
                return self._best_child.placePerson()
            else:
                self._left = type(self)(self._sort_vals[0], self._displace, self)
                self._right = type(self)(self._sort_vals[1], 
                                         self._displace + self._sort_vals[0] + 1,
                                         self)
                ret_val = self._sort_vals[:2] # min_val and max_val
                # now everyone should be updated...
                print ret_val
                self.update()
                return ret_val
                
        
        def sortVals(self):
            return self._sort_vals
        
        def hasChild(self):
            return self._left != None
        
        def _compHelper(self, v1, v2):
            '''if v1 > v2 1, v1 == v2 0, v1 < v2 -1'''
            if v1 > v2: return 1
            elif v1 == v2: return 0
            else: return -1
        
        def bestChild(self):
            '''this function dynamically recalculates best child'''
            assert self.hasChild()
            chooser = self._compHelper(self._left.sortVals()[0], 
                                       self._right.sortVals()[0])
            if chooser == 0:
                chooser = self._compHelper(self._left.sortVals()[1], 
                                           self._right.sortVals()[1])
            if chooser == 0:
                chooser = self._compHelper(self._left.sortVals()[2], 
                                           self._right.sortVals()[2])
            
            # now we will return the best child
            assert chooser != 0 # should never be 0 after this, actually
            return self._left if chooser > 0 else self._right
        
        def update(self):
            self._best_child = self.bestChild()
            new_vals = self._best_child.sortVals()
            if self._parent != None and self._sort_vals != new_vals:
                self._sort_vals = new_vals
                self._parent.update()

    def __init__(self, N):
        '''defines tree for search'''
        self._root = self.treeNode(N, 0, None)
    
    def addPerson(self):
        '''returns the min(lr) and max(lr) of new person'''
        return self._root.placePerson()

def solver(N, K):
    pre_iters = math.log(K, 2)
    init_vals = singleManSolver(N)
    if K == 1:
        return init_vals
    iter_dict = mydict()
    iter_dict[init_vals[0]] += 1
    iter_dict[init_vals[1]] += 1
    copy_dict = mydict()
    for i in xrange(int(pre_iters)-1): # process up to previous generation
        for key in iter_dict.keys():
            new_vals = singleManSolver(key)
            copy_dict[new_vals[0]] += iter_dict[key]
            copy_dict[new_vals[1]] += iter_dict[key]
            del iter_dict[key]
        for key in copy_dict.keys():
            iter_dict[key] = copy_dict[key]
        copy_dict = mydict()
    # now turn to process 2^(pre_iters)th person to K
    larger_key = max(iter_dict.keys())
    smaller_key = min(iter_dict.keys())
    if K-2**int(pre_iters) < iter_dict[larger_key]:
        return singleManSolver(larger_key)
    else:
        return singleManSolver(smaller_key)
    

def main():
    t_val = input('')
    for t_idx in xrange(t_val):
        N, K = map(int, raw_input('').split())
        #solve_tree = descTree(N)
        #for i in xrange(K-1):
            #solve_tree.addPerson()
        answ = solver(N, K)
        print 'Case #%d: %d %d' % (t_idx+1, answ[1], answ[0])

main()
#print 's:', solver(999, 487)
#solve_tree = descTree(999)
#for i in xrange(486):
    #solve_tree.addPerson()
#print 't:', solve_tree.addPerson()

#for num in xrange(1, 100):
    #print 's:', solver(100, num)
    #cha = int(100)
    #solve_tree = descTree(cha)
    
    #for i in xrange(num-1):
        #solve_tree.addPerson()
    #print 't:', solve_tree.addPerson()