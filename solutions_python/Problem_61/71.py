import time

print (time.ctime())

N_LIMIT = 30
MODULO = 100003

# pre-processing


def factorial (n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

def binomial (n,k):
    if k > n:
        return 0
    return factorial (n)// (factorial(k)*factorial (n-k))



intermediate_results = [[None]*(N_LIMIT) for i in range(N_LIMIT)]
for set_maximal_value in range(2,N_LIMIT):
    intermediate_results[set_maximal_value][1] = 1


for set_length in range(2,N_LIMIT):
    for set_maximal_value in range(2,N_LIMIT):
        # calculate intermediate_results[set_maximal_value][set_length]
        intermediate_results[set_maximal_value][set_length] = 0
        for next_subset_length in range(1,set_length):
            diff_values = set_maximal_value - set_length
            diff_lengths = set_length - next_subset_length
            binom = binomial (diff_values-1, diff_lengths-1)
            subset_poss = intermediate_results[set_length][next_subset_length]
            all_possibilities = (binom*subset_poss) % MODULO
            intermediate_results[set_maximal_value][set_length] += all_possibilities
            intermediate_results[set_maximal_value][set_length] %= MODULO
                

results = [0]*N_LIMIT
for value in range(2,N_LIMIT):
    for set_length in range(1,N_LIMIT):
        results[value] += intermediate_results[value][set_length]
        results[value] %= MODULO







# processing

f_in = open('c:/temp/codejam/round1b/problem_c/C-small-attempt1.in')
f_out = open('c:/temp/codejam/round1b/problem_c/C-small-attempt1.out','w')

T = int(f_in.readline())
for case in range(1,T+1):
    n = int (f_in.readline())
    f_out.write('Case #' + str(case) + ': ' + str(results[n]) + '\n')

f_out.close()
f_in.close()

print (time.ctime())

