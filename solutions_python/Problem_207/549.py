import sys

def rep_replace(end, RG_rep, BO_rep, YV_rep):
    R_f = False
    B_f = False
    Y_f = False
    ret = list()
    for c in end:
        if c == 'R' and not R_f:
            ret.append(RG_rep)
            R_f = True
        elif c == 'B' and not B_f:
            ret.append(BO_rep)
            B_f = True
        elif c == 'Y' and not Y_f:
            ret.append(YV_rep)
            Y_f = True
        else:
            ret.append(c)
    return "".join(ret)

def max_index(counts, cur):
    #print(counts)
    big_index = -1
    big = 0
    for index, count in enumerate(counts):
        
        if index != cur and count > big:
            big_index = index
            big = count
    
    if big_index == -1:
        return None
    
    return big_index

def three_string(R, B, Y):
    ret = ["R"]
    lookup = dict()
    lookup[0] = "R"
    lookup[1] = "B"
    lookup[2] = "Y"
    counts = [R - 1,B,Y]
    cur = 0
    while sum(counts) > 0:
        cur = max_index(counts, cur)
        #print(cur)
        if cur is None:
            return None
        counts[cur] -= 1
        ret.append(lookup[cur])
        
        
    return "".join(ret)

def ring(counts):
    R,O,Y,G,B,V = counts

    R_l = R - G
    B_l = B - O
    Y_l = Y - V    
    
    if sum([B,O,Y,V]) == 0:
        if R == G:
            return "RG" * R
    
    elif sum([G,R,Y,V]) == 0:
        if B == O:
            return "BO" * B
        
    elif sum([G,R,B,O]) == 0:
        if Y == V:
            return "YV" * Y
        
    elif R_l >= 1 and B_l >= 1 and Y == V == 0:
        if R_l == B_l:
            return "RG" * G + "RB" * B_l + "OB" * O
        
    elif R_l >= 1 and B == 0 == O and Y_l >= 1:
        if R_l == Y_l:
            return "RG" * G + "RY" * Y_l + "VY" * V
        
    elif R == 0 == G and B_l >= 1 and Y_l >= 1:
        if B_l == Y_l:
            return "BO" * O + "BY" * Y_l + "VY" * V
        
    elif R_l >= 1 and B_l >= 1 and Y_l >= 1:
        RG_rep = "RG" * G + "R" 
        BO_rep = "BO" * O + "B" 
        YV_rep = "YV" * V + "Y"
        end = three_string(R_l, B_l, Y_l)
        if end is not None:
            return rep_replace(end, RG_rep, BO_rep, YV_rep)
    
    return "IMPOSSIBLE"  

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        N, R, O, Y, G, B, V = (int(val) for val in in_file.readline().strip().split())
        
        #Call func for solution
        sol = ring([R,O,Y,G,B,V])
        out_file.write("Case #{}: {}\n".format(case, sol))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'B-sample'
        name = 'B-small-attempt0'
        #name = 'B-large'
        file_input = open(path + name + '.in', 'r')
        out_full_name = path + name +'.out'
        if alt_out:
            out_full_name = path + name + "naive" +'.out'            
        file_output = open(out_full_name,'w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
