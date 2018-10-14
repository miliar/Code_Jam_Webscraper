import math


def ample_syrup_solve(N, K, radii, heights):
    indices = range(N)
    indices.sort(key=lambda x: radii[x])
    heights = [heights[x] for x in indices]
    radii.sort()
    #print radii, heights
    best_base = K-1
    best_stacks = []
    for i in range(K -1):
        best_stacks.append(2 * math.pi * radii[i] * heights[i])
    best_score = math.pi * radii[K-1]**2 + 2 * math.pi * radii[K-1] * heights[K-1]
    best_score += sum(best_stacks)
    #print best_score
        
    for i in xrange(K, N):
        if K > 1:
            candidate_stack = 2 * math.pi * radii[i-1] * heights[i-1]
            #print best_stacks
            if candidate_stack > min(best_stacks):
                best_stacks.remove(min(best_stacks))
                best_stacks.append(candidate_stack)
            #print best_stacks
        candidate_base = math.pi * radii[i]**2 + 2 * math.pi * radii[i] * heights[i]
        if candidate_base + sum(best_stacks) > best_score:
            best_score = candidate_base + sum(best_stacks)
        #print best_score
    return best_score


def ample_syrup_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        inputs = f.readline().split()
        N = int(inputs[0])
        K = int(inputs[1])

        radii = []
        heights = []
        for j in xrange(N):
            inputs = [int(x) for x in f.readline().split()]
            radii.append(inputs[0])
            heights.append(inputs[1])            

        sol = ample_syrup_solve(N, K, radii, heights)
        #print sol
        str_sol = " ".join([str(x) for x in [sol]])
        output_f.write("Case #" + str(i) + ": " + str_sol + "\n")
    return 1

ample_syrup_main("A-large.in", "A-large.out")
