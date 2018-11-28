#!/usr/bin/env python3

count = int(input())
for x in range(1,count+1):
    n = int(input())
    n_blocks = []
    nums = input().split(" ")
    for i in range(0,n):
        n_blocks.append(float(nums[i]))
    k_blocks = []
    nums = input().split(" ")
    for i in range(0,n):
        k_blocks.append(float(nums[i]))
    n_blocks.sort()
    k_blocks.sort()

    n_war_win = 0
    n_dwar_win = 0

    n_copy = n_blocks[:]
    k_copy = k_blocks[:]
    n_spare = []
    k_spare = []
    while True:
        changed = False
        while len(n_copy) > 0 and len(k_copy) > 0:
            #print (n_copy, k_copy, n_spare, k_spare)
            if len(n_copy) == 0:
                k_spare.append(k_copy[-1])
                k_copy = k_copy[:-1]

            elif len(k_copy) == 0:
                n_spare.append(n_copy[-1])
                n_copy = n_copy[:-1]

            elif n_copy[-1] > k_copy[-1]:
                n_spare.append(n_copy[-1])
                n_copy = n_copy[:-1]
            else:
                changed = True
                n_copy = n_copy[:-1]
                k_copy = k_copy[:-1]



        if len(k_spare) == 0:
            n_war_win += len(n_spare)

        if len(n_spare) == 0 and len(k_spare) == 0:
            break


        n_copy = n_spare[:]
        k_copy = k_spare[:]
        n_copy.sort()
        k_copy.sort()
        n_spare = []
        k_spare = []


    for i in range(0,len(n_blocks)):
        if n_blocks[i] > k_blocks[i]:
            #n_dwar_win += 1
            pass
    
    #print (n_blocks, k_blocks)
    while len(n_blocks) > 0 and len(k_blocks) > 0:
        if len(k_blocks) == 0:
            break
        if n_blocks[0] < k_blocks[0]:
            n_blocks = n_blocks[1:]
            k_blocks = k_blocks[:-1]
        else:
            n_dwar_win += 1
            n_blocks = n_blocks[1:]
            k_blocks = k_blocks[1:]

    print ("Case #" + str(x) + ": " + str(n_dwar_win) + " " + str(n_war_win))
