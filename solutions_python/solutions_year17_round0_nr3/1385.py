def ms(N, K):
    #print("***********")
    #print("N: " + str(N))
    #print("K: " + str(K))
    if K < 1:
        #print("EAGER  RETURN")
        return None
    
    middle = -1
    right_advantage = False

    if N % 2 == 0:
        middle = (N/2)-1
        right_advantage = True
    elif N % 2 != 0:
        middle = N/2

    """print("middle: " + str(middle))
    if right_advantage:
        print("Advantage: Right")
    else:
        print("Advantage: Left")"""
        
    left_stalls = middle
    right_stalls = N-left_stalls-1

    K -= 1
    left_people = -1
    right_people = -1
    if right_advantage:
        if K % 2 == 0:
            right_people = K/2
            left_people = K-right_people
        else:
            right_people = (K/2)+1
            left_people = K-right_people
    else:
        if K % 2 == 0:
            left_people = K/2
            right_people = K-left_people
        else:
            left_people = (K/2)+1
            right_people = K-left_people
            
    #print("left_stalls: " + str(left_stalls))
    #print("right_stalls: " + str(right_stalls))
    #print("left_people: " + str(left_people))
    #print("right_people: " + str(right_people))

    left_sol = ms(left_stalls, left_people)
    right_sol = ms(right_stalls, right_people)

    #print(left_sol)
    #print(right_sol)

    if not left_sol and not right_sol:
        solution = [max(left_stalls, right_stalls), min(left_stalls, right_stalls)]
    elif not left_sol:
        solution = right_sol
    elif not right_sol:
        solution = left_sol
    else:
        if left_sol[0] <= right_sol[0] and left_sol[1] <= right_sol[1]:
            solution = left_sol
        else:
            solution = right_sol

    #print("Solution: ")
    #print(solution)
    return solution

def main():
    with open('C-small-2-attempt0.in', 'r') as f:
        rows = f.readlines()
        tests = int(rows[0])
        solutions = []
        for i in xrange(1, tests+1):
            row = rows[i].strip()
            splitted = row.split(' ')
            N = int(splitted[0])
            K = int(splitted[1])
            solution = ms(N, K)
            solutions.append(solution)

        with open('C-small-2-attempt0.out', 'w') as f:
            line_number = 1
            for line in solutions:
                f.write("Case #{0}: {1} {2}\n".format(str(line_number), line[0], line[1]))
                line_number += 1

main()
