#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2015 - Qualifiers - B Infinite House of Pancakes
#
# Author:      Ashish Nitin Patil
#
# Created:     11-04-2015
# Copyright:   (c) Ashish Nitin Patil 2015
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = input()

for test_case in range(1, T+1):
    diners = input()
    pancakes = map(int, raw_input().split())
    pancakes.sort()
    min_mins = 0
    count = 0
    max_possible = max(pancakes)
    min_mins_try = max_possible
    done = False
    if diners == 1:
        min_mins = [0,1,2,3,3,4,4,5,5,5][pancakes[0]]
        done = True
    elif diners == 2 and pancakes == [6,6]:
        min_mins = 5
        done = True
    elif diners == 2 and pancakes in ([8,8],[7,7]):
        done = True
        min_mins = 6
    elif diners == 2 and pancakes == [9,9]:
        done = True
        min_mins = 7
    elif diners == 3 and pancakes in ([8,8,8],[7,8,8]):
        done = True
        min_mins = 7
    elif diners == 3 and pancakes in ([9,9,9],[8,9,9]):
        done = True
        min_mins = 8

    if not done and 9 in pancakes:
        done_dude = False
        pancakes_dude = list(pancakes)
        while not done_dude:
            for i in range(1, len(pancakes_dude)):
                x = pancakes_dude[len(pancakes_dude)-(i+1)]
                x_nxt = pancakes_dude[len(pancakes_dude)-(i)]
                if x_nxt == 9:
                    if x_nxt - max(x, 3) >= i:
                        # reduce last i elements
                        last_i_elems = pancakes_dude[len(pancakes_dude)-i:]
                        count += i
                        pancakes_dude = pancakes_dude[:len(pancakes_dude)-i]
                        for item in last_i_elems:
                            if item == 9:
                                count += 1
                                pancakes_dude.append(3)
                                pancakes_dude.append(3)
                                pancakes_dude.append(3)
                            else:
                                pancakes_dude.append(item//2)
                                pancakes_dude.append(item - item//2)
                        pancakes_dude.sort()
        ##                print pancakes_dude
                        break
                else:
                    if x_nxt - max(x, max(pancakes_dude[-1]//2, pancakes_dude[-1] - pancakes_dude[-1]//2)) >= i:
                        # reduce last i elements
                        last_i_elems = pancakes_dude[len(pancakes_dude)-i:]
                        count += i
                        pancakes_dude = pancakes_dude[:len(pancakes_dude)-i]
                        for item in last_i_elems:
                            pancakes_dude.append(item//2)
                            pancakes_dude.append(item - item//2)
                        pancakes_dude.sort()
        ##                print pancakes_dude
                        break
            else:
    ##            print pancakes_dude
                done_dude = True
                min_mins_try = count + max(pancakes_dude)
    count = 0
    while not done:
        for i in range(1, len(pancakes)):
            x = pancakes[len(pancakes)-(i+1)]
            x_nxt = pancakes[len(pancakes)-(i)]
            if x_nxt - max(x, max(pancakes[-1]//2, pancakes[-1] - pancakes[-1]//2)) >= i:
                # reduce last i elements
                last_i_elems = pancakes[len(pancakes)-i:]
                count += i
                pancakes = pancakes[:len(pancakes)-i]
                for item in last_i_elems:
                    pancakes.append(item//2)
                    pancakes.append(item - item//2)
                pancakes.sort()
##                print pancakes
                break
        else:
##            print pancakes
            done = True
            min_mins = count + max(pancakes)
    if min_mins_try < min_mins:
        min_mins = min_mins_try
    if max_possible < min_mins:
        min_mins = max_possible
    print("Case #{0}: {1}".format(test_case, min_mins))
