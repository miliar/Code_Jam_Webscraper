import fileinput

memoized_state = {}

def bruteforce_solver(diners_state):
    #print "In solver, state:",diners_state
    if diners_state in memoized_state:
        return memoized_state[diners_state]
    if len(diners_state) == 0:
        return 0
    #Option 1 - everyone eats a pancake
    sol_state = bruteforce_solver(tuple(x-1 for x in diners_state if x > 1))
    #Option 2 - split the biggest pile (will get more pancakes eaten over time than any other option)
    for i in range(len(diners_state)):
        if diners_state[i] > 1:
            element_val = diners_state[i]
            other_elements = diners_state[:i]+diners_state[i+1:]
            for j in range(1,min(element_val/2+1,element_val-1)):
                new_tuple = other_elements + (j, element_val-j) 
                opt_val = bruteforce_solver(tuple(sorted(new_tuple,
                                                         reverse=True)))
                #print "Split element %d, got new tuple:" % i , new_tuple, "and opt_val=%d"%opt_val
                sol_state = min(sol_state,opt_val)
    memoized_state[diners_state] = sol_state+1
    return memoized_state[diners_state]

def solve():
    it = fileinput.input()
    num_cases = int(it.next())
    for i in range(num_cases):
        d = int(it.next())
        diners_state = tuple(sorted([int(x) for x in it.next().split()]))
        print "Case #%d: %d" % (i+1, bruteforce_solver(diners_state))

if __name__ == "__main__":
    solve()
