#!/usr/bin/python
import sys

def calc_ans(tree, word):
    count = 0
    if len(tree) == 0:
        return 1
    if len(word) == 0:
        return 0
    for c in word[0]:
        if c in tree:
            count += calc_ans(tree[c], word[1:])
    return count

def main():
    handle = file(sys.argv[1])
    l, d, n = map(lambda x: int(x), handle.readline().split())

    words_tree = {}

    for i in range(d):
        word = handle.readline()[:-1]
        curr_node = words_tree
        for c in word:
            if c not in curr_node:
                curr_node[c] = {}
            curr_node = curr_node[c]

    for case_no in range(1,n+1):
        broke_word = handle.readline()[:-1]

        #  Prepare word list:
        l = []
        in_sublist = False
        for c in broke_word:
            if c == "(":
                in_sublist = True
                l.append([])
                continue

            if c == ")":
                in_sublist = False
                continue

            if in_sublist:
                l[-1].append(c)
            else:
                l.append([c])
            
        print "Case #%d: %d" % (case_no, calc_ans(words_tree, l))

main()
