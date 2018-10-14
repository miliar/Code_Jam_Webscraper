
import itertools

def test_combinations(lines, size):
    best_true_sum = 0
    
    g = itertools.combinations(range(len(lines)), size)
    for i in g:

        sum_in = 0
        sum_out = 0
        true_sum_in = 0
        
        nxt = 0
        for j in range(len(lines)):
            if nxt < len(i) and j == i[nxt]:
                sum_in = sum_in ^ lines[j]
                true_sum_in = true_sum_in + lines[j]
                nxt = nxt+1
            else:
                sum_out = sum_out ^ lines[j]
                
        if sum_in == sum_out and true_sum_in > best_true_sum:
            best_true_sum = true_sum_in
        
    return best_true_sum

def alg(lines):
    print(lines)
    sum_val = sum(lines)
    score = 0
    
    for i in range(1, len(lines)):
        new_score = test_combinations(lines, i)
        if (new_score > score):
            score = new_score

    if score == 0:
        return ['NO']
    return [score]

if __name__ == '__main__':
    fname = "C"
#    f = open(fname+".in.txt", "r")
    f = open("/home/lawford/Desktop/"+fname+"-small-attempt0.in")
# f = open("/raid/downloads/firefox/"+fname"+-large.in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
    unnecessary_count = f.readline()
    piece1 = f.readline()
    while piece1 != '':
        result = alg([int(x) for x in piece1.split(' ')])
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        
        unnecessary_count = f.readline()
        piece1 = f.readline()

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.close()
    f.close()
