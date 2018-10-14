import sys

def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up.
    Borrowed from Peter Norvig's Design of Computer Programs course
    on Udacity.com."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

def is_solvable(Amote, l2):
    if len(l2) == 0: return True
    for mote in l2:
        if Amote > mote: Amote += mote
        else: return False
    return True

def add_mote(Amote, l2):
    '''Adds the mote that minimizes nops needed if we were to pursue
    the path of strictly adding motes to the game -- no subtraction'''
    i = 0
    while i < len(l2):
        if Amote > l2[i]: Amote += l2[i]
        else: break # l2[i] cannot be consumed by Amote
        i += 1
    return l2[:i] + (Amote - 1,) + l2[i:]

def subtract_mote(l2):
    return l2[:-1]

@memo
def get_num_ops(Amote, l2):
    if is_solvable(Amote, l2): return 0
    return 1 + min(get_num_ops(Amote, subtract_mote(l2)), get_num_ops(Amote, add_mote(Amote, l2)))

def main():
    input = open(sys.argv[1], 'r')
    output = open(sys.argv[2] + '.out', 'w')
    
    case = 1
    ncases = int(input.readline().strip())
    
    while case <= ncases:
        line = input.readline()
        l1 = map(int, line.strip().split()) # list
        line = input.readline()
        l2 = tuple(sorted(map(int, line.strip().split()))) # tuple
        # delete all motes if Amote == 1
        nops = len(l2) if l1[0] == 1 else get_num_ops(l1[0], l2)
        output.write('Case #{}: {}'.format(case, nops) + '\n')
        case += 1
    
    output.close()
    input.close()
    

if __name__ == '__main__':
    main()

'''Unused code:

def find_next_op(l1, l2, nops):
    Amote = l1[0]
    if Amote < 2: return l2, len(l2) # delete all in l2
    for mote in l2:
    
def find_min_operations(l1, l2):
    # l1: l1[0] = size of Armin's mote; l1[1] = number of other motes
    # l2: the N sizes of the other motes (ints)
    nops = 0
    while not is_solvable(l1[0], l2):
        l2, nops = change_motes(l1, l2, nops)
    return nops

'''