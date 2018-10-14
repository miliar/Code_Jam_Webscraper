import sys, string;

#input format:
#T, then T lines like
#Number Surprising p t[1:N]

#example input 1 (expected output:3)
N = 3
S = 1
p = 5
totals = [15, 13,11]

#returns true if the total score could be composed of a surprising triplet
#that has a best individual score of p or better.
def hasSurprising(total, p):
    #starting point p or higher
    for first in range(p, 11):
        #second score offset by two to make surprising case
        for second in [first-2, first+2]:
            if second > 10 or second < 0:
                continue; #invalid second item, skip this case.
            #third point between first and second (can't be further away)
            third = total - (first + second);
            if third in range(min(first,second), min(11,max(first,second)+1)):
                #print first, second, third;
                return True;
    return False;

#returns true if the total score could be composed of a non-surprising triplet
#with a maximum score of p or over
def hasNormal(total, p):
    return total >= p+(p-1)*2;#assume this is correct & simpler.

    #set the first score to p or any value up to 10
    #then the second and third to first-1, first, first+1
    #to create all possible non-surprising triplets.
    #return if one normal triplet was found.
    #for first in range(p, 11):
    #    for second in range(first-1, first+2):
    #        for third in range(first-1, first+2):
    #            if first + second + third == total:
    #                return True;
    #return False;

#returns number of total scores that can have p or better in it,
#given that S of the len(T) scores are surprising.
#t is a list of total scores.


    
def solve(S, p, totals):
    results = [0, 0, 0];
    BOTH = 0;
    SURPRISING = 1;
    NORMAL = 2;
    
    for t in totals:
        normal = hasNormal(t,p);
        surprising = hasSurprising(t,p);
        if normal and surprising:
            results[BOTH]+=1;
        elif normal:
            results[NORMAL]+=1;
        elif surprising:
            results[SURPRISING]+=1;
    return results[BOTH]+results[NORMAL]+min(S,results[SURPRISING]);

def intAll(l):
    for i in range(len(l)):
        l[i] = int(l[i]);
    return l;

T = int(sys.stdin.readline());
for i in range(1, T+1):
    line = string.split(sys.stdin.readline());
    N = int(line[0]);
    S = int(line[1]);
    p = int(line[2]);
    totals = intAll(line[3:]);
    print "Case #%d: %d" % (i, solve(S, p, totals));
