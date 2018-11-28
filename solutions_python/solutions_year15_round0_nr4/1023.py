__author__ = 'orin'
import math
round_up = lambda num: int(num + 1) if int(num) != num else int(num)

def richardWins(x,r,c):
    if x == 1:
        return False
    if x == 2 and r*c%2 ==0:
        return False
    if (r*c)%x != 0:
        return True
    if (r*c)/x == 2 and x > 3:
        return True
    if x > r and x > c:
        return True
    if (x > 2 ) and (c == 1 or r == 1):
        return True

    return False

def main():
    folder = 'C:\\Users\\New Editor\\Documents\\orin\\GoogleCodeJam\\2015\\QualificationRound\\'
    input_path = 'D-small-attempt8.in'
    out_path = 'D-small-attempt8.txt'
    with open(folder + input_path, 'r') as input_file:
        inp = input_file.read()

    #splits into the string into cases and removes the case numbers from the list
    inp = inp.split('\n')
    T = int(inp[0])
    inp.remove(inp[0])


    with open(folder + out_path, 'w') as out_file:
        for case in range(T):
            inp[case] = inp[case].split(' ')
            for i in range(len(inp[case])):
                inp[case][i] = int(inp[case][i])
            x = inp[case][0]
            r = inp[case][1]
            c = inp[case][2]

            if richardWins(x,r,c):
                answer = 'RICHARD'
            else:
                answer = 'GABRIEL'


            out_file.write('Case #{0}: {1}\n'.format(case+1, answer))
if __name__ == '__main__':
    main()

