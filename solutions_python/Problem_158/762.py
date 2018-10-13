from random import randint
import sys

def omnominoes(x, r, c,):
    if (r * c) % x != 0:
        return 'RICHARD'
    if (x > r) and (x > c):
        return 'RICHARD'
    if x > 6:
        return 'RICHARD'
    if x >= ((min(r, c) * 2) + 1):
        return 'RICHARD'
    if (x == 4) and ((r * c) == 8):
        return 'RICHARD'
    return 'GABRIEL'

def generate_test_data():
    cases = randint(5, 100)
    data = str(cases)

    for x in range(cases):
        data = '\n'.join([data, "{} {} {}".format(randint(1, 20), randint(1, 20), randint(1, 20))])

    print data
    return data

def test(test_runs):
    for i in range(test_runs):
        infile = open('p2_data_{}'.format(str(i)), 'w+')
        infile.write(generate_test_data())
        infile.close()

        infile = open('p2_data_{}'.format(str(i)))
        outfile = open('p2_output_{}'.format(str(i)), 'w+')

        for j in range(int(infile.readline())):
            data = infile.readline().strip().split(' ')
            winner_winner_chicken_dinner = omnominoes(int(data[0]), int(data[1]), int(data[2]))
            outfile.write('Case #{}: {}\n'.format(str(j+1), winner_winner_chicken_dinner))
        outfile.close()
        infile.close()

if __name__ == '__main__':
    infile = open(sys.argv[1])
    outfile = open(sys.argv[1] + '_out', 'w+')

    for i in range(int(infile.readline())):
        data = infile.readline().strip().split(' ')
        winner_winner_chicken_dinner = omnominoes(int(data[0]), int(data[1]), int(data[2]))
        outfile.write('Case #{}: {}\n'.format(str(i+1), winner_winner_chicken_dinner))
    outfile.close()