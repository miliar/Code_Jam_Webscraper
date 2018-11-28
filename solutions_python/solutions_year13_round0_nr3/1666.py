import math
import itertools

def get_number_of_fair_and_square(A, B):
    #Need to look for suitable palindromes betwee the sqrt.
    sqrtB = math.ceil(math.sqrt(B)) #Round up just to be safe.
    possible_candidates = [1,2,3] #Include these square roots as well, they are special cases
    max_digits = len(list(str(sqrtB)))
    if max_digits >= 2:
        for i in range(2, max_digits + 1):
            others = generate_candidates(i)
            possible_candidates += others
    #print(possible_candidates)
    fair_and_squares = eliminate_unwanted_candidates(possible_candidates, A, B)
    return(len(fair_and_squares))

def list_to_int(lis):
    return  int(''.join(map(str,lis)))

def generate_candidates(size):
    pals = []
    perms = list(itertools.product([0,1,2], repeat=math.ceil(size / 2)))
    for perm in perms:
        if perm[0] == 0:
            continue #Don't consider anything containing leading zeroes
        lis = list(perm)
        #Make the 2 possible pals
        if size % 2 == 0:
            a = 0
        else:
            a = 1
        for j in reversed(range(len(lis) - a)): #Can put - 1
            lis.append(lis[j])
        pals.append(list_to_int(lis))       
    return pals    
    

def eliminate_unwanted_candidates(list_of_numbers, A, B):
    kept = []
    for num in list_of_numbers:
        square = num * num
        if is_palindrone(square) and square >= A and square <= B:
            kept.append(square)
    return kept
        
        
def is_palindrone(N):
    digits = list(str(N))
    mid_point = int(len(digits)/2)
    for i in range(mid_point + 1):
        if not(digits[i] == digits[len(digits) - i - 1]):
            return False
    return True
    

def read_and_process_test_cases():
    file = open("qual_c.txt")
    T = int(file.readline())
    cur_case = 1
    while cur_case <= T:
        line = file.readline()
        A, B = line.split()
        result = get_number_of_fair_and_square(int(A), int(B))
        print("Case #" + str(cur_case) + ": " + str(result))
        cur_case += 1
        
read_and_process_test_cases()