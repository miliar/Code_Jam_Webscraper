f = open('A-small-attempt0.in','r')
input_file = [x.strip() for x in f.readlines()]
f.close()

#number of cases
nC = int(input_file.pop(0))
cases = []
idx = 0
for _ in range(nC):
    nW = int(input_file[idx])
    case = [x for x in input_file[idx+1:idx+1+nW]]
    idx = idx+1+nW
    cases.append(case)

#result = True
#case = cases[2]
def solve_case(case):
    nW = len(case)
    words = case
    letter_seqs = [[word[0]] + [word[idx] for idx in range(1,len(word)) if word[idx] != word[idx-1]] for word in words]
    for idx in range(1,nW):
        if letter_seqs[idx] != letter_seqs[idx-1]:
            return 'Fegla Won'
    #possible - only one letter sequence
    letter_seq = letter_seqs[0]
    #count number of each letter
    #word = words[0]
    letter_counts = []
    for word in words:
        letter_count = [0 for _ in range(len(letter_seq))]
        jdx = 0
        for (idx,letter) in enumerate(letter_seq):
            while word[jdx] == letter:
                letter_count[idx] += 1
                if jdx == len(word)-1:
                    break
                else:
                    jdx += 1
        letter_counts.append(letter_count)
    
    mean_letter_count = [int(round(average([letter_count[idx] for letter_count in letter_counts]))) for idx in range(len(letter_seq))]
    
    moves = sum([sum([abs(x-y) for x,y in zip(letter_count,mean_letter_count)]) for letter_count in letter_counts])
    return str(moves)




f = open('A_test_solution.txt', 'w')    
for case_idx,case in enumerate(cases):
    f.write('Case #' + str(case_idx+1)+ ': ' + solve_case(case) +'\n')
f.close()
