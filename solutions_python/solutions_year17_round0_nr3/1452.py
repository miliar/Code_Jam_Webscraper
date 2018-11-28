
# coding: utf-8

# In[90]:

def solve(num_stalls, num_people):
    mem = dict();

    def DistributionOf(N, k):
        if N in mem:
            return mem[N];
        if N < 1:
            return {0: 1};
        if k <= 0:
            return {N: 1};
        if N % 2 == 1:
            d = DistributionOf((N-1)/2, k-1);
            mem[(N-1)/2] = d;
            return {z: 2*d.get(z, 0)  for z in set(d)};
        else:
            d1 = DistributionOf(N/2-1, k-1);
            d2 = DistributionOf(N/2, k-1);
            mem[N/2-1] = d1;
            mem[N/2] = d2;
            return {z: d1.get(z, 0) + d2.get(z, 0) for z in set(d1) | set(d2)}
        
    level = len(bin(num_people))-3
    level_index = num_people - 2**level
    stall_available = DistributionOf(num_stalls, level)
    sorted_stall_available = [(z, stall_available[z]) for z in sorted(set(stall_available), key=lambda x: -x)]

    if level_index >= sorted_stall_available[0][1]:
        largest_space = sorted_stall_available[1][0]
    else:
        largest_space = sorted_stall_available[0][0]

    if largest_space == 0:
        return(int(0), int(0));
    if largest_space % 2 == 1:
        return(int((largest_space-1)/2), int((largest_space-1)/2));
    else:
        return(int(largest_space/2), int(largest_space/2-1));


# In[98]:

inputs = """4 2
5 2
6 2
1000 1000
1000 1
492 468
999 497
345 323
518 409
395 317
999 999
1000 256
365 288
500 255
788 741
1000 511
999 487
1 1
1000 128
5 1
2 1
3 2
312 291
317 243
429 373
999 404
715 688
500 245
3 1
500 101
500 128
444 380
278 238
836 782
999 256
2 2
1000 512
653 577
1000 504
746 669
1000 255
500 117
525 425
347 286
955 873
999 511
999 498
1000 500
500 2
4 1
999 128
500 248
500 1
500 198
794 750
999 127
999 488
500 500
1000 127
999 499
315 282
500 252
882 694
603 542
721 614
500 244
756 731
854 811
416 317
733 683
927 756
500 249
500 116
1000 489
1000 498
999 506
999 255
999 998
560 544
882 820
1000 2
673 591
1000 304
1000 499
999 2
999 1
500 256
879 749
1000 488
412 358
526 463
500 127
657 643
858 749
999 512
500 499
1000 999
450 392
825 618
500 250""".split('\n')


# In[101]:

for i, p in enumerate(inputs):
    ans = solve(int(p.split()[0]), int(p.split()[1]));
    print("Case #"+str(i+1)+": "+str(ans[0])+ " "+str(ans[1]))


# In[102]:

from heapq import heappush, heappop

def bruteForce(N, n):
    Q = [-1*N];
    num_people = n
    while num_people -1 > 0:
        num_stalls = heappop(Q)
        if num_stalls % 2 == 1:
            heappush(Q, (num_stalls+1)/2);
            heappush(Q, (num_stalls+1)/2);
        if num_stalls % 2 == 0:
            heappush(Q, (num_stalls/2));
            heappush(Q, (num_stalls/2)+1);

        num_people-=1

    space_available = -1*Q[0]
    if space_available == 0:
        return (0, 0)
    if space_available % 2 == 1:
        return(int((space_available -1) / 2), int((space_available -1) / 2))
    else:
        return(int(space_available/2), int(space_available/ 2-1))
    


# In[103]:

for i, p in enumerate(inputs):
    ans = solve(int(p.split()[0]), int(p.split()[1]));
    b_ans = bruteForce(int(p.split()[0]), int(p.split()[1]));
    #print(str(p)+"   Case #"+str(i+1)+": "+str(ans[0])+ " "+str(ans[1]))
    if(str(ans) != str(b_ans)):
        print(str(p)+ "Fast:" + str(ans) + ", Brute:" + str(b_ans));


# In[ ]:



