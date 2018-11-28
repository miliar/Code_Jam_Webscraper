import sys

def main():
    fname = sys.argv[1]
    with open(fname) as f:
        lines = f.readlines()
    n_cases = int(lines[0])
    case = 1
    i = 1
    while i < len(lines):
        line = lines[i][:-1]
        splitted = line.split(" ")
        rows = int(splitted[0])
        columns = int(splitted[1])
        i = i + 1
        matrix = []
        for j in range(rows):
            line = lines[i][:-1]
            last = '?'
            string = ""
            for k in range(columns):
                c = line[k]
                if last == '?' and c != '?':
                    string = c * (k + 1)
                    last = c
                elif c == '?' and last != '?':
                    string = string + last
                elif c != '?':
                    string = string + c
                    last = c
            if last != '?':
                string = string + last * (columns - len(string))
            matrix.append(string)
            i = i + 1
        first = False
        for j in range(rows):
            if matrix[j] == "" and first:
                matrix[j] = matrix[j - 1]
            elif matrix[j] != "" and not first:
                for k in range(j):
                    matrix[k] = matrix[j]
                first = True
            elif matrix[j] != "":
                first = True
        print("Case #%i:" % case)
        for m in matrix:
            print(m)
        case = case + 1

if __name__ == "__main__":
    main()
