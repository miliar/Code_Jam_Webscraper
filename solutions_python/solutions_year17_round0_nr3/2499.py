# Author: Hurturk Yagmur
# Codejam Qualification Round 2017 - Problem C - Bathroom stalls

def print_case(n, result):
    print("Case #%d: %s" % ((n+1), str(result)))

def analyze_all(stalls, minlr_data, maxlr_data):
    for i, s in enumerate(stalls):
        if s == "o":
            minlr_data[i] = -1 
            maxlr_data[i] = -1 
            continue
        k = i
        while stalls[k] != "o":
            k -= 1
        l_data = i - k - 1
        m = i
        while stalls[m] != "o":
            m += 1
        r_data = m - i - 1
        minlr_data[i] = min(r_data, l_data)
        maxlr_data[i] = max(r_data, l_data)


T = int(raw_input())

for case in range(0, T):
    n,ppl = map(lambda x: int(x), raw_input().split(" "))
    stalls = ["." for _ in range(0,n+2)]
    stalls[0] = "o"
    stalls[len(stalls)-1] = "o"
    minlr_data = [-1 for _ in range(0,n+2)]
    maxlr_data = [-1 for _ in range(0,n+2)]
    final_min = -1
    final_max = -1

    while ppl != 0:
        analyze_all(stalls, minlr_data, maxlr_data)
        max1 = max(minlr_data)
        indices = [i for i, x in enumerate(minlr_data) if x == max1]
        #print indices

        final_min = max1
        if len(indices) == 1:
            stalls[indices[0]] = "o"
            #print indices[0]
            final_max = maxlr_data[indices[0]]
            ppl -= 1
            #print "stalls: ", stalls
            #print minlr_data
            #print maxlr_data
            continue

        final_choice = -1
        final_index = -1
        for occurence in indices:
            if maxlr_data[occurence] > final_choice:
                final_choice = maxlr_data[occurence]
                final_index = occurence
                final_max = final_choice

        stalls[final_index] = "o"
        ppl -= 1
        #print "stalls: ", stalls
        #print minlr_data
        #print maxlr_data


    print_case(case, str(final_max) + " " + str(final_min))
