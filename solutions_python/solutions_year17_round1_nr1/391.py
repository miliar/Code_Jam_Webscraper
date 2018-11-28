#import pdb

def naive_solve(N):
    pass

def all_question_marks(row):
    for x in row:
        if x != '?':
            return False

    return True

def fill_previous(i, c, row):
    i -= 1
    while i >= 0 and row[i] == '?':
        row[i] = c
        i -= 1

def fill_row(row):
    for i, c in enumerate(row):
        if c != '?':
            fill_previous(i, c, row)

    #find final non question mark character
    for i in range(len(row) - 1, -1, -1):
        if row[i] != '?':
            #make rest of list the same
            for j in range(i+1, len(row)):
                row[j] = row[i]

            break


def solve(A):
    # fill in non all question mark rows
    for row in A:
        if all_question_marks(row):
            continue
        else:
            fill_row(row)

    #find first non all question mark row
    i = 0 
    while all_question_marks(A[i]):
        i += 1

    #make all preceding rows the same as first non all question marks row
    for j in range(0, i):
        A[j] = [x for x in A[i]]

    for j in range(i, len(A)):
        if all_question_marks(A[j]): #make same as previous row
            A[j] = [x for x in A[j-1]]

    return A



def parse_test_case():
    R, C = [int(x) for x in input().strip().split()]
    A = []
    for _ in range(R):
        A.append([x for x in input().strip()])
    return A

def stress_test():
    from sys.stdout import write 
    for N in range(1, 10**18):
        write('\rTest Case: %d' % (N))
        if naive_solve(N) != solve(N):
            print()
            print('Failed with input', N, 'ans given =', solve(N), 'real answer =', naive_solve(N))
            break

    print()
    print('Done')

def main():
    T = int(input())

    for case_num in range(1, T+1):
        ans = solve(parse_test_case())
        print('Case #', case_num, ':', sep='')
        for row in ans:
            print(''.join(row))



if __name__ == '__main__':
    main()
    #stress_test()
