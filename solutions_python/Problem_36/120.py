# Google Code Jam 2009
# Qualification Round - "Welcome to Code Jam"
# Author: Richard Ledley
# Python 2.5

def count_times(str, sub, lookup):
    """
    Returns occurrences of sub in str.
    """
    # Empty strings contain 0 occurrences
    if str == "":
        return 0

    # Have we already calculated this?
    try:
        return lookup[(str,sub)]
    except KeyError:
        pass

    # If it's just a single character, the answer is
    # the number of times it appears
    if len(sub) == 1:
        lookup[(str,sub)] = str.count(sub)
        return lookup[(str,sub)]

    index = str.find(sub[0])

    # If we can't find the first character in the
    # substring, there are 0 occurrences
    if index  == -1:
        lookup[(str,sub)] = 0
        return lookup[(str,sub)]

    # return times we can complete starting with the index we've found
    # plus the times we can find the entire substring not using the
    # index we've found
    ans = count_times(str[index+1:], sub, lookup) +\
          count_times(str[index+1:], sub[1:], lookup)
    lookup[(str,sub)] = ans
    return lookup[(str,sub)]

print "File?"
file = open(raw_input())
file.readline()
WELCOME = "welcome to code jam"
x = 1
for l in file:
    line = l.rstrip()
    print "Case #%d: %04d" % (x, count_times(line, WELCOME, {})%10000)
    x += 1
