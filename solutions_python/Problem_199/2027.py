# Input: signs is the str, i is the index we're at and K is length of flipper
# returns true if there are not K chars between signs[i] and signs[len(signs)-1]
# includsive
def tooCloseToEnd(signs, i, K):
    numToEnd = len(signs) - i
    return numToEnd < K

# flips all elems of signs and returns new string with the flipped elems
def flip(signs):
    result = ""
    for char in signs:
        if(char == "-"):
            result += "+"
        else:
            result += "-"
    return result

# returns the smallest number of flips to get signs to all +
# only ever flipping K consecutive elems at a time
def getNumFlips(signs, K):
    numFlips = 0
    for i in xrange(len(signs)):
        currElem = signs[i]
        if(currElem == "-"):
            if(tooCloseToEnd(signs, i, K)):
                return "IMPOSSIBLE"
            else:
                newSegment = flip(signs[i:i+K])
                signs = signs[:i] + newSegment + signs[i+K:]
                numFlips += 1
    return numFlips


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  signs, K = raw_input().split(" ")  # read a list of integers, 2 in this case
  K = int(K)
  numFlips = getNumFlips(signs, K)
  print "Case #{}: {}".format(i, numFlips)
  # check out .format's specification for more formatting options