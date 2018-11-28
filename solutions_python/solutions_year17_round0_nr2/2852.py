#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     08/04/2017
# Copyright:   (c) user 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = str(raw_input())
        print "Case #{}: {}".format(i, tidy(n))

def tidy(s):
    '''string s'''
    n = []
    index = len(s)-1
    for i in xrange(index):
        if int(s[i]) > int(s[i+1]):
            index = i
            break
    else:
        return s
    for i in xrange(index,0,-1):
        if int(s[i]) != int(s[i-1]):
            index = i
            break
    else:
        index = 0
    if index > 0:
        n.append(s[:index])
    n.append(str(int(s[index])-1))
    n += ['9']*(len(s)-index-1)
    if int(n[0]) == 0:
        return ''.join(n[1:])
    else:
        return ''.join(n)


if __name__ == '__main__':
    main()
