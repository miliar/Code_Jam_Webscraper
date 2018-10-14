#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def update_nglist(word, words, nglist, c):
    for i in xrange(len(words)):
        if nglist[i]:
            continue
        for j in xrange(len(word)):
            if word[j] == c:
                # revealed
                if words[i][j] != c:
                    nglist[i] = 1
                    break
            elif words[i][j] == c:
                nglist[i] = 1
                break

def isRevelaedAnswer(nglist):
    n = 0
    for l in nglist:
        if not l:
            n = n + 1
    return n <= 1

def isAllRevealed(word, revealed):
    for i in xrange(len(word)):
        if not word[i] in revealed:
            return False
    return True

def simulate(word, words, list):
    lose = 0
    nglist = [0]*len(words)
    revealed = []
    # eliminate different len words
    for i in xrange(len(words)):
        if len(words[i]) != len(word):
            nglist[i] = 1

    for i in xrange(len(list)):
        for j in xrange(len(words)):
            if nglist[j]:
                continue
            if list[i] in words[j]:
                # choose the character
                break
        else:
            # nothing... skip
            continue
        # check
        if list[i] in word:
            revealed.append(list[i])
            if isAllRevealed(word, revealed):
                break
            # update nglist
            update_nglist(word, words, nglist, list[i])
            if isRevelaedAnswer(nglist):
                # no more words
                break
        else:
            # lose point
            for k in xrange(len(words)):
                if nglist[k]:
                    continue
                if list[i] in words[k]:
                    nglist[k] = 1
                if isRevelaedAnswer(nglist):
                    # no more words
                    break

            lose = lose + 1

    return lose

def doIt(words, list):
    best = -1
    answer = ''
    for word in words:
        result = simulate(word, words, list)
        if result > best:
            answer = word
            best = result
    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        n = map(int, f.readline().split())
        num_of_words = n[0]
        num_of_lists = n[1]
        words = []
        lists = []
        for j in range(num_of_words):
            words.append(f.readline().rstrip())
        for j in range(num_of_lists):
            lists.append(f.readline().rstrip())

        answer = []
        for list in lists:
            answer.append(doIt(words, list))

        print "Case #%d: %s" % (i+1, ' '.join(answer))

