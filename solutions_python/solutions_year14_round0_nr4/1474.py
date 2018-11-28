## Google Code Jam ##
## Qualification Round ##
## Problem D. Deceitful War ##

def run_case(lines):
    blocks = int( (lines[0].strip()) )
    n = [float(i) for i in lines[1].strip().split(' ')]
    k = [float(j) for j in lines[2].strip().split(' ')]

    war_score = war(n,k,blocks)
    d_war_score = d_war(n,k,blocks)

    return (d_war_score,war_score)

def war(n,k,blocks):
    n = n[:]
    k = k[:]
    n.sort()
    k.sort()
    
    score = 0
    for i in xrange(0,len(n)):
        n_val = n[i]
        k_chosen = -1
        for j in xrange(0,len(k)):
            if k[j] > n_val:
                k_chosen = j
                break
        if ( k_chosen == -1 ):
            k.pop(0)
            score += 1
        else:
            k.pop(j)
    return score

def d_war(n,k,blocks):
    n = n[:]
    k = k[:]
    n.sort()
    k.sort()

    return d_war_iterate(n,k,blocks,0)
    #return d_war_recurse(n,k,0)

def d_war_recurse(n,k,score):
    if ( len(n) == 0 ):
        return score
    ## Deceit
    new_n = n[1:]
    new_k = k[:-1]
    a1 = d_war_recurse(new_n,new_k,score)
    ## Truth
    a2 = -1
    if ( n[-1] > k[-1] ):
        new_n = n[:-1]
        new_k = k[:-1]
        a2 = d_war_recurse(new_n,new_k,score+1)
    return max(a1,a2)

def d_war_iterate(n,k,blocks,score):
    score = 0
    count = 0
    n = n[:]
    k = k[:]
    while count < blocks:
        ## Truth
        if ( n[-1] > k[-1] ):
            n = n[:-1]
            k = k[:-1]
            score += 1
        ## Deceit
        else:
            n = n[1:]
            k = k[:-1]

        count += 1
    return score

f = file('in_large.txt','r')

lines = f.readlines()

cases = int(lines[0].strip())
print "Number of cases", cases

out = file('out_large.txt','w')

in_length = 3

for case in xrange(0,cases):
    output = run_case(lines[case*in_length+1:(case+1)*in_length+1])
    out.write("Case #" + str(case+1) + ": " + str(output[0]) + " " + str(output[1]) + "\n")

f.close()
out.close()

