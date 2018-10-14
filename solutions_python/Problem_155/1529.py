import random
import sys

def ovation(audience):
    count = 0
    friends = 0

    for place in xrange(len(audience)):
        while not (count >= place):
            friends += 1
            count += 1
        count = count + int(audience[place])

    return friends

def generate_test_data():
    cases = random.randint(5, 100)
    data = str(cases)

    for x in range(cases):
        highest_shyness = random.randint(0,1000)
        data = '\n'.join([data, str(highest_shyness) + ' '])

        for y in range(highest_shyness+1):
            data = ''.join([data, str(random.randint(0,9))])

    return data

def test(test_runs):
    for i in range(test_runs):
        foo = open('p1_data_{}'.format(str(i)), 'w+')
        foo.write(generate_test_data())
        foo.close()

        foo = open('p1_data_{}'.format(str(i)))
        bar = open('p1_output_{}'.format(str(i)), 'w+')

        for j in range(int(foo.readline())):
            audience = foo.readline().split(' ')[1].strip()
            friends = ovation(audience)
            bar.write('Case #{}: {}\n'.format(str(j+1), str(friends)))
        bar.close()
        foo.close()

if __name__ == '__main__':
    infile = open(sys.argv[1])
    outfile = open(sys.argv[1] + '_out', 'w+')

    for i in range(int(infile.readline())):
        audience = infile.readline().split(' ')[1].strip()
        friends = ovation(audience)
        outfile.write('Case #{}: {}\n'.format(str(i+1), str(friends)))
    outfile.close()