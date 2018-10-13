from collections import namedtuple

Case = namedtuple("Case", "row layout")


def get_row_from_lines(lines):
    lines = iter(lines)
    row_index = int(lines.next()) - 1
    print row_index
    for row in range(row_index):
        lines.next()
    
    line = lines.next()
    
    for row in range(3 - row_index):
        lines.next()
    
    return set(int(x) for x in line.split(" "))


def get_options_from_case(lines):
    lines = iter(lines)
    row1 = get_row_from_lines(lines)
    row2 = get_row_from_lines(lines)
    print row1, row2
    return row1 & row2


def parse_input(lines):
    lines = iter(lines)
    number_of_cases = int(lines.next())
    results = []
    for case in range(number_of_cases):
        results.append(get_options_from_case(lines))
        
    return results
        

def main():
    with open("A-small-attempt0.in", "rb") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    print lines
    print parse_input(lines)
    results = []
    for n, result in enumerate(parse_input(lines), 1):
        output = "Case #%d: " % (n, )
        if len(result) == 0:
            output += "Volunteer cheated!"
        elif len(result) > 1:
            output += "Bad magician!"
        else:
            output += str(result.pop())
        results.append(output)
    with open("output.txt","wb") as f:
        f.write("\n".join(results))

if __name__ == '__main__':
    main()