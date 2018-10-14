import collections
import numbers
import unittest

def apprEqual(a, b):
    '''
    >>> apprEqual(1, 2)
    False
    >>> apprEqual(1, 1.00000000001)
    True
    '''
    tolerance = 1e-6
    if isinstance(a, numbers.Complex) or isinstance(b, numbers.Complex):
        return abs(a-b) <= 0.5 * tolerance * (abs(a) + abs(b))
    return a == b
        

class binomial_coef:
    '''
    >>> binomial_coef(6, 3)
    20
    '''
    
    def __init__(self):
        self.bin_cache = {}
    
    def __call__(n, k):
        if k == 0:
            return 1
        if n == 0: # we know k > 0
            return 0
        if (n, k) in self.bin_cache:
            return self.bin_cache[(n,k)]
        result = self.binomial_coef(n-1, k-1) + self.binomial_coef(n-1, k)
        self.bin_cache[(n,k)] = result
        return result
    

class Reader:
    '''
    
    '''
    def __init__(self, stream):
        self.stream = stream
        
    def get_line(self):
        return next(self.stream).rstrip('\n')

    def get_value(self, type_ = int):
        line = self.get_line()
        return type_(line)

    # sep == '' => treat line as an iterabe
    # sep == '\n' => multi-line
    # if types is not a sequence, it's assumed to be the type to be used for each value
    def get_list(self, types = int, sep = ' '):
        line = self.get_line()
        if sep == '':
            fields = list(line)
        else:
            fields = line.split(sep)
        if not isinstance(types, collections.Sequence):
            types = len(fields) * [types]
        return [types[i](f) for i, f in enumerate(fields)]

def process_input(in_stream, solver_factory, first_test = None, last_test = None):
    reader = Reader(in_stream)
    n_tests = reader.get_value()
    if first_test is None:
        first_test = 1
    if last_test is None:
        last_test = n_tests
    result = ''
    for current_test in range(1, n_tests + 1):
        solver = solver_factory(reader)
        if first_test <= current_test <= last_test:
            solution = solver.solve()
            result += 'Case #{}: {}\n'.format(current_test, solution)
            print('Case #{} solved.'.format(current_test))
    return result
            

class MustImplementInSubclass(Exception):
    pass

# rather than requiring functions (e.g., get_children) as parameters, we'll define them in subclass
# the advantages are: less parameter passing; and easier access to shared data of the state space

# we have to be careful how the equality for nodes is defined
# for example, if we encounter a node represented as [1, 3], is it the same as another node represented as [1, 3] but at a different location?
# we require that the node objects have appropriately defined equality and hash function; in the future, Graph may provide some assistance (e.g., a wrapper) when requested to help with this
class Graph:
    def __init__(self, root, get_children):
        self.root = root
        # if there's a lot (or infinitely many) branches, we need this to be an iterator
        # Python 3.3 might support it easier
        # we'll also be unable to do DFS; rather, we'll have to do something more heuristic-like
        self.get_children = get_children
    
    def get_children_with_backpointer(self, node):
        for child in self.get_children(node):
            yield (node, child) 
    
    #def dfs(self, root):
        #yield root
        #for node in self.get_children(root):
            #yield from self.dfs(node)
    
    # if the graph is not a tree, check_visit must be True
    # if the graph is a large implicit tree, check_visit should be False (otherwise all all nodes will have to be materialized)
    # if the graph is a small implicit tree or an explicit tree, check_visit is harmless but useless (except for one of the approaches to postorder traversal!)
    # storing a parent to each node is only a constant factor cost (O(depth)) so maybe we should make it standard rather than optional to simplify code?
    def idfs(self, root = None, check_visit = True, store_path = False): #check_visit = True?
        if root is None:
            root = self.root
        if check_visit:
            visited = set()
        if store_path:
            to_visit = [(root, None)]
        else:
            to_visit = [root]
        while to_visit:
            if store_path:
                node, parent = to_visit.pop()
            else:
                node = to_visit.pop()
            if check_visit:
                if node in visited:
                    continue
                visited.add(node)
            if store_path:
                children = list(self.get_children_with_backpointer(node))
                children.reverse()
                to_visit.extend(children)
                yield node, parent
            else:
                children = list(self.get_children(node))
                children.reverse()
                to_visit.extend(children)
                yield node # preorder
            
    def iter_dfs_postorder(self, root):
        pass
                
        


KEY, PREV, NEXT = range(3)

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[PREV]
            curr[NEXT] = end[PREV] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[NEXT] = next
            next[PREV] = prev

    def __iter__(self):
        end = self.end
        curr = end[NEXT]
        while curr is not end:
            yield curr[KEY]
            curr = curr[NEXT]

    def __reversed__(self):
        end = self.end
        curr = end[PREV]
        while curr is not end:
            yield curr[KEY]
            curr = curr[PREV]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = next(reversed(self)) if last else next(iter(self))
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

    def __del__(self):
        self.clear()                    # remove circular references

    #do we need these?
    #difference = property(lambda self: self.__sub__)
    #difference_update = property(lambda self: self.__isub__)
    #intersection = property(lambda self: self.__and__)
    #intersection_update = property(lambda self: self.__iand__)
    #issubset = property(lambda self: self.__le__)
    #issuperset = property(lambda self: self.__ge__)
    #symmetric_difference = property(lambda self: self.__xor__)
    #symmetric_difference_update = property(lambda self: self.__ixor__)
    #union = property(lambda self: self.__or__)
    #union_update = property(lambda self: self.__ior__)
    

# to get __hash__ and __eq__ return id(self)
class Reference:
    def __init__(self, item):
        self.item = item

class RemovalAPI:
    def add_removal_info(self, item, removal_info):
        try:
            references = item.__reference
        except AttributeError:
            references = item.__reference = {}
        references[Reference(self)] = removal_info
        
    def get_removal_info(self, item):
        try:
            references = item.__reference
            self_reference = Reference(self)
            return references[self_reference]
        except AttributeError:
            raise Exception('Cannot remove item {} from {}: no valid removal info found'.format(item, self))
        except KeyError:
            raise Exception('Cannot remove item {} from {}: no valid removal info found'.format(item, self))

        
class StandardizedList(list, RemovalAPI):
    def __iter__(self):
        for i in range(len(self)):
            item = self[i]
            self.add_removal_info(item, i)
            yield item
            
    def remove(self, item):
        removal_info = self.get_removal_info(item)
        del self[removal_info]
    
    def insert(self, item):
        self.append(item)
        
        
if __name__ == '__main__':
    unittest.main()