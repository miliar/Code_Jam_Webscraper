def create_triplet(score):
    tmp = score / 3
    if 3*tmp == score:
        return [tmp, tmp, tmp]
    if 3*tmp + 1 == score:
        return [tmp+1, tmp, tmp]
    return [tmp+1, tmp+1, tmp]

def is_candidate(triplet,p):
    score = sum(triplet)
    
    if (score - p) < 0:
        return False; 
    
    tmp = score - 3*p
    
    if tmp in range(-4,5):
        return True
    
    return False
    
def calculate(triplets,p,S):
    result = 0
    available = S
    for triplet in triplets:
        if (max(triplet) >= p):
            result = result + 1
            continue
        if available <= 0:
            continue
        if (is_candidate(triplet,p)):
            result = result + 1
            available = available - 1
                    
    return result


# return the number of max possibilities
def hanlde_input(input):
    input_list = input.split(" ")
    
    
    N = int(input_list[0])
    S = int(input_list[1])
    p = int(input_list[2])
    
    scores = input_list[3:]
    scores = [int(i) for i in scores]
    
    not_surprising_triplets = [create_triplet(score) for score in scores]
    
    result = calculate(not_surprising_triplets,p,S)
    
    return result


def solve():
    file_in = file("B-small-attempt0.in")
    file_out = file("B-small-attempt0.out","w")
    num_of_cases = int(file_in.readline())
    lines = []
    for i in range(num_of_cases):
        # read
        line = file_in.readline()
        
        # process
        result = hanlde_input(line)
        
        # write
        lines.append('Case #%s: %s\n' % (i+1,result))
    
    file_out.writelines(lines)
    file_out.close()

if __name__ == '__main__':
    solve()