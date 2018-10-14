def main():
    cases = read('A-small-attempt0.in')
    output = solve_all(cases)
    write(output)

def solve_all(cases):
    output = ''
    for x in range(len(cases)):
        output += 'Case #{}: {}\n'.format(x+1, solve_one(cases[x]))
    return output[:-1]

def write(s):
    file = open("output.txt", 'w')
    file.write(s)
    file.close()
    

def solve_one(case):
    #case of format:
    #[row, mat1, row, mat2]
    options = list(set(case[1][int(case[0])-1]) & set(case[3][int(case[2])-1]))
    if len(options) == 0:
        return "Volunteer cheated!"
    elif len(options) > 1:
        return "Bad magician!"
    else:
        return options[0]

def read(path):
    #returns list of the cases
    file = open(path, 'r')
    data = file.read()
    l = data.split('\n',1)
    lines = l[1].split('\n')
    cases = []
    for x in range(int(l[0])):
        case_string = lines[10*x:10*x+10]
        case = []
        case.append(case_string[0])
        case.append(lines_to_matrix(case_string[1:5]))
        case.append(case_string[5])
        case.append(lines_to_matrix(case_string[6:]))
        cases.append(case)
    file.close()
    return cases
    

def lines_to_matrix(lines):
    #converts 4 lines into 4x4 matrix
    mat = []
    for l in lines:
        mat.append(l.split(' '))
    return mat

if __name__ == "__main__":
    main()
