
class Stall(object):

    def __init__(self ):
        self.occupied = False
        self.r_buffer = None
        self.l_buffer = None

    def __str__(self):
        return 'O:{}, lB:{}, rB:{}'.format(self.occupied, self.l_buffer, self.r_buffer)

    def occupy(self):
        # set up a way to fall out
        self.occupied = True

    def get_min(self):
        return min(self.l_buffer, self.r_buffer)

    def get_max(self):
        return max (self.l_buffer, self.r_buffer)

def setup_stalls(n):
    """ returns List of linked Stall nodes"""
    # left guard
    focus = Stall()
    stalls = [focus]
    for ii in range(n):
        stalls.append(Stall())
    # right guard
    stalls.append(Stall())
    # Set initial weights
    occupy_right(stalls, 0)
    occupy_left(stalls, len(stalls) - 1)
    return stalls


def occupy_right(stalls, start_idx):
    for ii, idx in enumerate(xrange(start_idx, len(stalls))):
        stall = stalls[idx]
        if ii == 0:
            stall.occupy()
        elif stall.occupied:
            # Stop once an occupied stall is hit, nodes to the right are already up to date
            return
        else:
            stall.l_buffer = ii - 1


def occupy_left(stalls, start_idx):
    for ii, idx in enumerate(range(start_idx, 0, -1)):
        stall = stalls[idx]
        if ii == 0:
            stall.occupy()
        elif stall.occupied:
            return
        else:
            stall.r_buffer = ii - 1

def occupy(stalls, idx):
    occupy_right(stalls, idx)
    occupy_left(stalls, idx )



def test():
    stalls =  setup_stalls(1000)
    # n = pick_stall(stalls)
    # occupy(stalls, n)
    final = pick_stall(stalls)
    print stalls[final].get_max(), stalls[final].get_min()


def pick_stall(stalls):
    # Algo, find largest get_min
    # If tie, find largest get_max
    # if tie choose L
    candidates = get_min_indices(stalls)
    if len(candidates) == 1:
        return candidates[0]
    else:
        candidates = get_max_indices(stalls, candidates)
        if len(candidates) == 1:
            return candidates[0]
        elif candidates:
            # 0 - N indexing, smallest index is leftmost
            return min(candidates)
        else:
            return None


def get_max_indices(stalls, c_indices):
    # Finding the lowest get_max among c_indices
    candidates = []
    g_min = float('-inf')
    for idx in c_indices:
        stall = stalls[idx]
        # don't consider occupied
        if not stall.occupied:
            i_max = stall.get_max()
            if i_max > g_min:
                g_min, candidates = i_max, [idx]
            elif i_max == g_min:
                candidates.append(idx)
            else:
                continue
    return candidates


def get_min_indices(stalls):
    candidates = []
    g_max = float('-inf')
    # Finding the largest minimum
    for ii,stall in enumerate(stalls):
        # don't consider occupied
        if not stall.occupied:
            i_min = stall.get_min()
            if i_min > g_max:
                g_max, candidates = i_min, [ii]
            elif i_min == g_max:
                candidates.append(ii)
            else:
                continue
    return candidates


def process_input():
    # Skip number of test cases
    t = int(raw_input())  # read a line with a single integer
    for ii in xrange(1, t + 1):
        stall_count, people = [int(e) for e in raw_input().split()]
        stalls = setup_stalls(stall_count)
        for __ in range(1, people):
            n = pick_stall(stalls)
            occupy(stalls, n)
        final = pick_stall(stalls)
        if final:
            print('Case #{ii}: {n} {m}'.format(ii=ii,
                n=stalls[final].get_max(), m=stalls[final].get_min()))
        else:
            print('Case #{ii}: 0 0'.format(ii=ii))


if __name__ == '__main__':
    #test()
    process_input()