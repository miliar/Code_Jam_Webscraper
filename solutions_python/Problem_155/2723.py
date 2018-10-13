#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    T = cipher.split()
    Smax = int(T[0])
    audience = T[1]
    list_audience = list(audience)
    #print ("init SMax: %s" % str(Smax))
    #print ("init list: %s" % str(list_audience))

    # Expend zeros
    if len(list_audience) != int(Smax)+1:
        Smax=len(list_audience)-1

    #print ("SMax: %s" % str(Smax))
    #print ("list: %s" % str(list_audience))

    # process
    already_standing = 0
    result = 0

    # shy 0 must be present
    if (int(list_audience[0])>0):
        already_standing += int(list_audience[0])
        #print ("0: nothing, already_stand=0, now stading=%d" % (int(list_audience[0])))
    else:
        result += 1
        already_standing += 1
        #print ("0: add(1), already_stand=0, now stading=%d" % (1))

    for i in range(1, Smax+1):
        if ((already_standing >= i) | (int(list_audience[i]) == 0)):
            #print ("%d: nothing, already_stand=%d, now stading=%d" % (i, already_standing, already_standing+int(list_audience[i])))
            already_standing += int(list_audience[i])
        else:
            cur_added_people = i - already_standing
            #print ("%d: add(%d), already_stand=%d, now stading=%d" % (i, cur_added_people, already_standing, already_standing+cur_added_people+int(list_audience[i])))
            result += cur_added_people
            already_standing += cur_added_people + int(list_audience[i])

    return result

def main():
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))


if __name__ == "__main__":
    main()
