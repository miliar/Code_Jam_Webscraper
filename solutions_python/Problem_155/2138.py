def solve(line):
    line_list = line.split()
    max_shy = int(line_list[0])
    people = map(int, list(line_list[1]))
    added = 0
    if len(people) == 1:
        return added
    for i in range(1, max_shy+1):
        if people[i] > 0:
            people_before = sum(people[:i])
            if people_before < i:
                this_add = i - people_before
                added += this_add
                people[i-1] += this_add
    return added


def run():
    input = open('A-large.in')
    output = open('ouput2.txt', 'w')

    num_cases = int(input.readline())

    for case in range(num_cases):
        result = solve(input.readline())
        line = "Case #%d: %d\n" % (case+1, result)
        output.write(line)

    input.close()
    output.close()

if __name__ == '__main__':
    run()