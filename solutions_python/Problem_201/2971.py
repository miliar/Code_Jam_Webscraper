# A bathroom has N+2 stalls
# The outer ones are PERMANENTLY occupied by guards [100001]

#When someone enters, they choose a stall as FAR from others as possible
#deterministically

#For each empty stall S they compute two values LS and RS
#each of which is number of empty stalls between S and the closest occupied stall left/right respectively
#They consider a set of stalls with the FARTHEST closests neighbor
#   the S for which min(LS, RS) is maximal

#if there is one such stall, they choose it
#otherwise they choose the one among those where max(LS, RS) is maximal
#still tied? they choose the leftmost one

#K people will enter the bathroom
#When the last person choose their stall S, what will the values of
#   max(LS, RS) and
#   min(LS, RS) be?

#### INPUT
#First line is T, T lines follow
#Each line describes a test case with two ints N and K
# N = There are N+2 numbers of stalls (as left and right are occupied)
# K = how many people will come in

#### OUTPUT
#For each case output 'Case #x: y z' where
#x is case starting from 1
#y is max(LS, RS)
#z is min(LS, RS) for the last person to choose a stall

def caseOutput(x, y, z):
    """Construct a string like Case #X: Y Z"""
    return 'Case #' + str(x) + ': ' + str(y) + ' ' + str(z);

def calcLeftDistance(stalls, s):
    leftStalls = stalls[:s];
    for i,o in reversed(list(enumerate(leftStalls))):
        if(o == 1):
            return s - i - 1;

def calcRightDistance(stalls, s):
    rightStalls = stalls[s+1:];
    for i,o in enumerate(rightStalls):
        if(o == 1):
            return i;

def calcBoth(stalls, s):
    ls = calcLeftDistance(stalls, s);
    rs = calcRightDistance(stalls, s);
    return ls,rs;

filename = 'C-small-1-attempt1';
# filename = 'sample';
inFile = open('./'+filename+'.in', 'r');
outFile = open('./'+filename+'.out', 'w');

cases = int(inFile.readline());
for x in range(1,cases+1):
    n,k = inFile.readline().split(' ');
    n = int(n);
    k = int(k);

    # print('N = ' + str(n));
    # print('K = ' + str(k));

    #early optimization: if K==N we're done and output 0 0
    if(n==k):
        # print(caseOutput(x,0,0));
        outFile.write(caseOutput(x,0,0) + '\n');
        continue;

    stalls = [0 for i in range(0,n)];
    stalls.insert(0, 1);
    stalls.append(1); #1 .. nx0 .. 1

    for p in range(0,k):

        #TODO understand python's map/lambda/filter combination to do this shit efficiently
        #cant be that hard to just get the INDICES of all the 1s
        occs = [];
        for s in range(0, n+2):
            #filter to only keep the indexes of occupied stalls (so we can avg them)
            if(stalls[s] == 1):
                occs.append(s);

        bestDiff = -1;
        bestStall = {'stall':-1, 'left':-1, 'right':-1, 'max':-1, 'min':-1};
        for i in range(1,len(occs)):
            prev = occs[i-1];
            curr = occs[i];

            diff = curr - prev;
            if(diff == 1):
                # diff 1 so no point right ?
                continue;

            if(diff <= bestDiff):
                # already had bestdiff better than diff, so keep leftmost one
                continue;

            mid = (curr+prev)//2;
            left = mid - (prev+1);
            right = curr-mid-1;
            mmax = max(left,right);
            mmin = min(left,right);

            bestDiff = diff;
            bestStall = {'stall':mid, 'left':left, 'right':right, 'max':mmax, 'min':mmin};

        # print('best');
        # print(bestStall);
        stalls[bestStall['stall']] = 1;
        # print(stalls);
    #

    # print('\n\n');
    # print(caseOutput(x, bestStall['max'], bestStall['min']));
    outFile.write(caseOutput(x, bestStall['max'], bestStall['min']) + '\n');

inFile.close();
outFile.close();
