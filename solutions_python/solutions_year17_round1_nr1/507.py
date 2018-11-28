def ContainsNonQuestionMarkCharacters(row):
    for c in row:
        if c != '?':
            return True
    return False

def FirstNonQuestionMarkCharacter(row):
    for c in row:
        if c != '?':
            return c

def FirstRowWithANonQuestionMarkCharacter(rows):
    for row in rows:
        if ContainsNonQuestionMarkCharacters(row):
            return row

def PartitionRow(row):
    current_letter = FirstNonQuestionMarkCharacter(row)
    result = ''
    for c in row:
        if c == '?' or c == current_letter:
            result += current_letter
        else:
            current_letter = c
            result += current_letter
    return result

def Solve(num_rows, num_cols, grid):
    current_row = FirstRowWithANonQuestionMarkCharacter(grid)
    result = []
    for row in grid:
        if not ContainsNonQuestionMarkCharacters(row) or row == current_row:
            result.append(PartitionRow(current_row))
        else:
            current_row = PartitionRow(row)
            result.append(PartitionRow(current_row))
    return result

num_problems = int(raw_input())
for problem_num in xrange(1, num_problems + 1):
    num_rows, num_cols = [int(s) for s in raw_input().split(" ")]
    grid = []
    for row_num in xrange(1, num_rows + 1):
        grid.append(raw_input())

    solution = Solve(num_rows, num_cols, grid)

    print "Case #{}:".format(problem_num)
    for row in solution:
        print row