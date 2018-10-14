def fair(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False

def square(num):
    if fair(num):
        sq = int(num**0.5)
        if sq*sq == num:
            if fair(sq):
                return True
    return False

def main():
    f = open('G:/Study/Programming/Code Jam/2013/C-small-attempt0.in', 'r')
    #f = open('G:/Study/Programming/Code Jam/trial.txt', 'r')
    g = open('G:/Study/Programming/Code Jam/2013/output3_small.txt', 'w')
    #g = open('G:/Study/Programming/Code Jam/output_trial.txt', 'w')
    no_test_cases = int(f.readline())
    for test_case in range(1,no_test_cases+1):
        A, B = f.readline().split()
        A, B = int(A), int(B)
        count = 0
        for each in range(A,B+1):
            if square(each):
                count += 1
        g.writelines('Case #'+str(test_case)+': '+str(count)+chr(10))

if __name__ == '__main__':
    main()
