vowels = ["a", "e", "i", "o", "u"]

def process_test_case(name, n, case):
    name_list = list(name)
    number_of_substrings = 0
    L = len(name_list)
    max_count_back = 0 #How far can we go back? (to avoid double ups)
    for i in range(L - n + 1): #Starting at each position... is there n cons?
        #Need to check if there is a length n sequence starting at i...
        is_seq = True
        for j in range(i, i+n):
            cur_letter = name_list[j]
            if cur_letter in vowels:
                is_seq = False
                break
        #If there is...
        if is_seq:
            num_of_starting_points = i + 1 - max_count_back
            num_of_ending_points = L - (i + n - 1)
            number_of_substrings += num_of_starting_points * num_of_ending_points
            max_count_back = i + 1
    print("Case #" + str(case) + ": " + str(number_of_substrings))
            
file = open("data.txt")
T = int(file.readline())
for i in range(T):
    name, n = file.readline().split()
    process_test_case(name, int(n), i+1)            
        
