import sys
import math

def _circle_area(rad):
    return rad ** 2

def _side_area(rad, height):
    return 2 * rad * height

def max_area(cakes, limit):
    #sort cakes by side area
    cakes.sort(key = lambda cake: cake[2])
    cakes.reverse()
    
    best_tot = 0
    #take each cake one at a time as given.
    for i in range(len(cakes)):
        take_cake = cakes[i]
        rad_best = take_cake[0]
        tot = take_cake[2]
        taken = 1
        
        for j in range(len(cakes)):
            if i == j:
                continue
            if taken >= limit:
                break
            cand = cakes[j]
            taken += 1
            tot += cand[2]
            if cand[0] > rad_best:
                rad_best = cand[0]
        
        tot += _circle_area(rad_best)
        
        if taken == limit and tot > best_tot:
            best_tot = tot
            
    return best_tot * math.pi
    
    

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        num_cakes, num_choose = (int(val) for val in in_file.readline().strip().split())
        cakes = []
        for _ in range(num_cakes):
            rad, height = (int(val) for val in in_file.readline().strip().split())
            cakes.append((rad, height, _side_area(rad, height)))
        sol = max_area(cakes, num_choose)
        #Call func for solution
        out_file.write("Case #{}: {}\n".format(case, sol))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'A-sample'
        #name = 'A-small-attempt0'
        name = 'A-large'
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
        
        
