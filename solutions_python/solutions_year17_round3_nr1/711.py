#!/usr/bin/python
import sys
import math

PROBLEM = 'a'

dataset = ''

if len(sys.argv) == 2:
    dataset = sys.argv[1]


def get_file(argv):
    if len(argv) == 1:
        return "{}.in".format(PROBLEM)
    else:
        return "{}_{}.in".format(PROBLEM, dataset)

def get_file_out(argv):
    if len(argv) == 1:
        return "{}.out".format(PROBLEM)
    else:
        return "{}_{}.out".format(PROBLEM, dataset)

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def get_last_number(N):
    past_numbers = set()
    goal = set([i for i in xrange(1, 10)])
    found = set()
    multiplier = 1
    current_number = N
    while current_number not in past_numbers:
        digits = [int(d) for d in str(current_number)]
        found.update(digits)
        if len(found) == 10:
            return current_number
        past_numbers.add(N)
        multiplier = multiplier + 1
        current_number = N * multiplier
    return None

def get_d(p):
    return p[0]*2

def get_r(p):
    return p[0]

def get_h(p):
    return p[1]

# def get_exposed(p, p_after):
#     return p_after.

def get_top(p):
    return (get_r(p) ** 2)# * math.pi

def get_side(p):
    return 2 * get_r(p) * get_h(p) #* math.pi

def get_new(p_top, p_bottom):
    return get_top(p_bottom) - get_top(p_top) + get_side(p_bottom)

def get_exposed(N, K, P):#, i, j, k):
    mx = 0.0
    #if k == 1:
    #    mx += math.pi * (get_r(p) ** 2)
    # mx = get_top(P[0]) + get_side(P[0])
    # S = [[mx, 1]]
    mx_i = 0
    k_i = 1
    i_i = 2
    # first top
    S = [
        [{'e': get_top(P[0])+get_side(P[0]), 'k': 1, 'i': 0}]
    ]
    mx = get_top(P[0])+get_side(P[0])
    for i in xrange(1, N):
        S.append([])
        t = get_top(P[i])
        s = get_side(P[i])
        if K == 1:
            mx = max(mx, t+s)
        else:
            S[i].append({'e': t+s, 'k': 1, 'i': i})
        for j in xrange(0, len(S[i-1])):
            prev = S[i-1][j]
            prev_mx = prev['e']
            prev_k = prev['k']
            prev_i = prev['i']
            prev_t = get_top(P[prev_i])

            if prev_k == K:
                mx = max(mx, prev_mx)
            else:
                #dont use level
                S[i].append(prev)
                #use level
                # print get_new(P[prev_i], P[i])
                new_a = prev_mx + get_new(P[prev_i], P[i])
                new_k = prev_k + 1

                if new_k == K:
                    #print 'new_k==K', new_a
                    mx = max(mx, new_a)
                else:
                    S[i].append({'e': new_a, 'k':new_k, 'i':i})
        #print S
    return mx


    

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        N, K = map(int, f.readline().strip().split(' '))
        P = []
        for i in xrange(0, N):
            P.append(map(float, f.readline().strip().split(' ')))
        P.sort()
        exposed = get_exposed(N, K, P)
        print_answer(t, "{0:.9f}".format(exposed*math.pi), f_out)


if __name__ == "__main__":
    main(sys.argv)
