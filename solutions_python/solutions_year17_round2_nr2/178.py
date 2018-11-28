
def solve_min(B, R, Y):
    chars = ["B", "R", "Y"]
    char_count = {"B" : B, "R" : R, "Y" : Y}
    sol = ""
    
    max_char = max(chars, key=lambda x: char_count[x])
    if 2 * char_count[max_char] > B + R + Y:
        return "IMPOSSIBLE"
    sol += max_char
    char_count[max_char] -= 1
    
    for i in xrange(1, B + R + Y):
        other_chars = [x for x in chars if x != sol[-1]]
        next_pick = max(other_chars, key=lambda x: char_count[x])
        if char_count[other_chars[0]] == char_count[other_chars[1]]:
            if other_chars[0] == max_char:
                next_pick = max_char
            if other_chars[1] == max_char:
                next_pick = max_char                
        #print other_chars, next_pick, char_count, sol[-1], sol
        sol += next_pick
        char_count[next_pick] -= 1
    return sol
#print solve_min(2, 2, 2)
def stable_neighbours_solve(N, R, O, Y, G, B, V):
    if R == 0 and G == 0 and B == 0 and O == 0:
        if Y == V:
            sol = ""
            for i in xrange(Y):
                sol += "YV"
            return sol
        else:
            return "IMPOSSIBLE"
    if Y == 0 and V == 0 and B == 0 and O == 0:
        if R == G:
            sol = ""
            for i in xrange(R):
                sol += "RG"
            return sol
        else:
            return "IMPOSSIBLE"
    if R == 0 and G == 0 and Y == 0 and V == 0:
        if B == O:
            sol = ""
            for i in xrange(B):
                sol += "BO"
            return sol
        else:
            return "IMPOSSIBLE"
    B_star = B - O
    if B_star <= 0 and O > 0:
        return "IMPOSSIBLE"
    R_star = R - G
    if R_star <= 0 and G > 0:
        return "IMPOSSIBLE"
    Y_star = Y - V
    if Y_star <= 0 and V > 0:
        return "IMPOSSIBLE"

    small_sol = solve_min(B_star, R_star, Y_star)
    if small_sol == "IMPOSSIBLE":
        return "IMPOSSIBLE"
    big_sol = ""
    used_first = []
    for char in small_sol:
        if char not in used_first:
            if char == "B":
                added = "B"
                for j in xrange(O):
                    added += "OB"
                used_first.append("B")
                big_sol += added
            if char == "R":
                added = "R"
                for j in xrange(G):
                    added += "GR"
                used_first.append("R")
                big_sol += added        
            if char == "Y":
                added = "Y"
                for j in xrange(V):
                    added += "VY"
                used_first.append("Y")
                big_sol += added
        else:
            big_sol += char
    return big_sol

def stable_neighbours_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        inputs = f.readline().split()
        N = int(inputs[0])
        R = int(inputs[1])
        O = int(inputs[2])
        Y = int(inputs[3])
        G = int(inputs[4])
        B = int(inputs[5])
        V = int(inputs[6])

        sol = stable_neighbours_solve(N, R, O, Y, G, B, V)
        #print R, O, Y, G, B, V
        #print sol
        wrong_n = {"B" : ["B", "G", "V"],
                   "R" : ["R", "O", "V"],
                   "Y" : ["Y", "G", "O"],
                   "G" : ["G", "V", "G", "B", "Y"],
                   "V" : ["G", "V", "G", "B", "R"],
                   "O" : ["G", "V", "G", "R", "Y"]                   
                   }
        #if sol != "IMPOSSIBLE":        
        #    for i in xrange(0, len(sol) - 1):
        #        if sol[i + 1] in wrong_n[sol[i]]:
        #            print "Error"
        #    if sol[-1] in wrong_n[sol[0]]:
        #        print R, O, Y, G, B, V
        #        print sol
        #        print "Error"
                
        
        output_f.write("Case #" + str(i) + ": " + str(sol) + "\n")
    return 1

stable_neighbours_main("B-large.in", "B-large.out")
