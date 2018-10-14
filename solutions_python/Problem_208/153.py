# pylint: disable=missing-docstring
import sys


def problem(horses, cities, queries):
    distances = [x[0][1] for x in cities if x]
    total_distances = [0]
    for x in distances:
        total_distances.append(total_distances[-1] + x)
    dist_func = lambda x, y: total_distances[y] - total_distances[x]

    table = [0]
    for nextCity in range(1, len(cities)):
        possibilities = []
        for startCity, startTime in enumerate(table):
            if dist_func(startCity, nextCity) > horses[startCity][0]:
                continue
            time = dist_func(startCity, nextCity) / horses[startCity][1]
            possibilities.append(startTime + time)
        table.append(min(possibilities))
    return table[-1]


def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]

def intsplit(s):
    return [int(x) for x in s.split(" ")]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile)
            numCities, numQueries = intsplit(case)
            horses = []
            for _ in range(numCities):
                horses.append(intsplit(nextline(infile)))
            cities = []
            for _ in range(numCities):
                conns = []
                c = intsplit(nextline(infile))
                for n in range(numCities):
                    if c[n] != -1:
                        conns.append((n, c[n]))
                cities.append(conns)
            queries = []
            for _ in range(numQueries):
                queries.append([x - 1 for x in intsplit(nextline(infile))])
            result += 'Case #{}: {}\n'.format(1 + run, problem(horses, cities, queries))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
