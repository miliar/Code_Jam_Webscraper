#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    in_file = open("D-large.in", mode='r')
    out_file = open("D-large.out", mode='w')

    T = int(in_file.readline())
    
    for i in range(T):
        N = int(in_file.readline())
        N_blocks = [float(x) for x in in_file.readline().strip().split()]
        K_blocks = [float(x) for x in in_file.readline().strip().split()]
        N_blocks.sort()
        K_blocks.sort()

        result_war = war(N_blocks, K_blocks)
        result_deceitful = deceitful(N_blocks, K_blocks)

        out_file.write("Case #" + str(i+1) + ": " + str(result_deceitful) + " " + str(result_war) + "\n") 

    in_file.close()
    out_file.close()

def war(N_blocks, K_blocks):
    NN = list(zip(N_blocks, ['N']*len(N_blocks)))
    KK = list(zip(K_blocks, ['K']*len(K_blocks)))
    all_blocks = NN + KK
    all_blocks.sort(key = lambda tup: tup[0])

    score = 0;
    N_count = 0
    K_count = 0
    for block in all_blocks:
        if block[1] == 'N':
            N_count += 1
        else:
            K_count += 1

        if block[1] == 'K' and K_count > (N_count + score):
            score += 1

    return score
    
def deceitful(N_blocks, K_blocks):
    NN = list(zip(N_blocks, ['N']*len(N_blocks)))
    KK = list(zip(K_blocks, ['K']*len(K_blocks)))
    all_blocks = NN + KK
    all_blocks.sort(key = lambda tup: tup[0])

    score = 0;
    N_count = 0
    K_count = 0
    N_used = 0
    for block in all_blocks:
        if block[1] == 'N':
            N_count += 1
            if N_used > 0:
                N_used -=1
        else:
            K_count += 1

        if block[1] == 'K' and (((len(N_blocks) - N_count) - N_used) > 0):
            score += 1
            N_used += 1

    return score
    
if __name__ == '__main__':
    main()