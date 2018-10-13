import sys

def last_y_z(n, k):
    stalls = [(True, i, n-i-1) for i in xrange(n)]
    for person in xrange(k):
        index, min_val, max_val = getChoice(n,stalls)
        stall_to_take = stalls[index]
        stalls[index] = (False,stall_to_take[1], stall_to_take[2])
        stalls = update(stalls, index)
        if person == k -1:
            return max_val, min_val

def update(stalls, index):
    n = len(stalls)
    empty_stall_right = 0
    empty_stall_left = 0
    for left in xrange(index-1, -1, -1):
        stall = stalls[left]
        if stall[0]:
            stalls[left] = (True, stall[1], empty_stall_right)
            empty_stall_right += 1
        else:
            break

    for right in xrange(index+1, n):
        stall = stalls[right]
        if stall[0]:
            stalls[right] = (True, empty_stall_left, stall[2])
            empty_stall_left +=1
        else:
            break
    return stalls

def getChoice(n,stalls):
    index = n + 1
    min_val = -sys.maxint-1
    max_val = -sys.maxint-1
    for i in xrange(n):
        stall = stalls[i]
        if stall[0]:
            curr_min = min(stall[1], stall[2])
            curr_max = max(stall[1], stall[2])

            if curr_min == min_val:
                # priority max
                if curr_max > max_val:
                    index = i
                    max_val = curr_max
                # if equal max, priority left
                elif curr_max == max_val:
                    if i < index:
                        index = i
                        max_val = curr_max

            elif curr_min > min_val:
                index = i
                max_val = curr_max
                min_val = curr_min
    return index, min_val, max_val




if __name__ == '__main__':
    with open("C-small-1-attempt0.in", "r") as f:
        t = int(f.readline())
        for i in xrange(1, t + 1):
            tup = f.readline().split()
            n = int(tup[0])
            k = int(tup[1])
            result = last_y_z(n,k)
            print "Case #" + str(i)+": " + str(result[0]) + " " + str(result[1])
