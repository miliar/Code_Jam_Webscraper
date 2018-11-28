

def core_training_solve_small(units, probs):
    if units >= len(probs) - sum(probs):
        return 1
    counter = 0

    while units > 10 ** (-10):
        counter += 1
        if counter % 100 == 0:
            print counter, units
        #print units, probs
        prob_vals = list(set(probs))
        prob_vals.sort()
        min_prob = prob_vals[0]
        if len(prob_vals) > 1:
            next_prob = prob_vals[1]
        else:
            next_prob = 1
        min_count = probs.count(min_prob)
        if units >= min_count * (next_prob - min_prob):
           units -= min_count * (next_prob - min_prob)
           for i in range(len(probs)):
               if probs[i] == min_prob:
                   probs[i] = next_prob
        else:
            extra = units / min_count
            for i in range(len(probs)):
                if probs[i] == min_prob:
                    probs[i] += extra
            units = 0

    final_prob = 1
    for prob in probs:
        final_prob *= prob

    return final_prob

def core_training_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        print i
        inputs = f.readline().split()
        N = int(inputs[0])
        K = int(inputs[1])
       
        inputs = [float(x) for x in f.readline().split()]
        units = inputs[0]

        probs = [float(x) for x in f.readline().split()]

        #print N, K, units, probs
        sol = core_training_solve_small(units, probs)
        #print sol
        str_sol = " ".join([str(x) for x in [sol]])
        output_f.write("Case #" + str(i) + ": " + str_sol + "\n")
    return 1

core_training_main("C-small-1-attempt1.in", "C-small-1-attempt1.out")
