import sys
sys.setrecursionlimit(100000)

def get_spacing(stall_list, index):
    i = stall_list.index(1)
    left = 0
    for l in range(i+1, len(stall_list)):
        if stall_list[l]:
            break
        else:
            left += 1
    right = 0
    for r in range(i-1, 0, -1):
        if stall_list[r]:
            break
        else:
            right += 1

    return left, right

def get_middle(n, m):
    l = range(n, m+1)
    return l[len(l)/2-1]

def find_max_spacing(stall_list):
    space_track = {}
    counter = 0
    for i in range(0, len(stall_list)):
        if stall_list[i]:
            if counter in space_track:
                pass
            else:
                space_track[counter] = (i-counter, i)
            counter = 0
        else:
            counter += 1
    return space_track[max(space_track.keys())]

def assign_stalls(stalls, people):
    stall_list = [-1] + [0] * stalls + [-1]
    #print stall_list
    while people > 0:
        l, r = find_max_spacing(stall_list)
        #print "max", l, r
        i = get_middle(l, r)
        #print "middle", i
        stall_list[i] = people
        #print stall_list
        people -= 1

    return get_spacing(stall_list, 1)

def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        stalls, people = [int(s) for s in raw_input().split()]
        #print stalls, people
        #obvious cases
        #
        #all of the stalls are taken
        # if stalls == people:
        #     l, r = 0, 0
        # elif people == 1:
        #     # only person goes in, check even/odd, and grab the middlest
        #     if stalls % 2 == 0:
        #         l, r = stalls/2, stalls/2-1
        #     else:
        #         l ,r = stalls/2, stalls/2
        # # and the hard cases
        # else:
        l, r = assign_stalls(stalls, people)

        print "Case #{}: {} {}".format(i, l ,r)

if __name__ == '__main__':
    main()
