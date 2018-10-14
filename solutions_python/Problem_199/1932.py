import collections

def flip(s, k, i):
    tmp = [t for t in s]
    tmp[i:i+k] = [not t for t in tmp[i:i+k]]
    return tmp

def check_goal(s):
    for i in s:
        if not i:
            return False
    return True

def convstr(v):
    a = ''
    for i in v:
        if i:
            a = a + '+'
        else:
            a = a + '-'
    return a

def goodness(v):
    return sum([1 if i else 0 for i in v])


def flip_pancakes(s, k):
    s = [i == '+' for i in s]
    state = [s]
    q = collections.deque()
    q.append(state)
    maxlen = 0

    lookupdict = {}
    lookupdict[convstr(s)] = 0

    while len(q) > 0:
        tmp = q.popleft()
        if check_goal(tmp[-1]):
            return len(tmp) - 1
        else:
            if len(tmp) > maxlen:
                maxlen = len(tmp)
                # print "maxlen: %s" % maxlen

            # print("processing %s" % convstr(tmp[-1]))
            for i in range(len(s) - k + 1):
                before = goodness(tmp[-1])
                new = flip(tmp[-1], k, i)
                after = goodness(new)
                if new not in tmp:
                    if convstr(new) in lookupdict:
                        if len(tmp) >= lookupdict[convstr(new)]:
                            continue
                    lookupdict[convstr(new)] = len(tmp)
                    # print("adding %s" % convstr(new))
                    tmptmp = [i for i in tmp]
                    tmptmp.append(new)
                    q.append(tmptmp)
                    if after - before == k:
                        break
                    
    return 'IMPOSSIBLE'



if __name__ == '__main__':

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      s, k = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
      print "Case #{}: {}".format(i, flip_pancakes(s, int(k)))
      # check out .format's specification for more formatting options