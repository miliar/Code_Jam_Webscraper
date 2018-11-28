from codejam import readfile

def sequence_count(word):
    cur_char = None
    result = []
    for char in word:
        if char != cur_char:
            cur_char = char
            result.append([char, 1])
        else:
            char, count = result[-1]
            result[-1] = [char, count+1]
    return result

def solve(words):
    template = sequence_count(words[0])
    solution = template[:]
    count = 1
    for word in words[1:]:
        seq = sequence_count(word)
        # Verfiy word is doable
        if len(seq) != len(template):
            return -1
        for template_count, word_count in zip(template, seq):
            if template_count[0] != word_count[0]:
                return -1
        # update solution count
        for solution_count, word_count in zip(solution, seq):
            solution_count[1] = (solution_count[1]*count + word_count[1])/(count + 1.)
        count += 1
    total = 0
    for word in words:
        seq = sequence_count(word)
        for word, solution_count in zip(seq, solution):
            total += abs(round(solution_count[1])-word[1])
    return int(total)
            

def readproblem(lines):
    count = int(lines[0])
    return lines[count+1:], lines[1:count+1]

lines = readfile()[1:]

case_no = 1
while lines:
    lines, problem = readproblem(lines)
    solution = solve(problem)
    if solution == -1:
        solution = "Fegla Won"
    print "Case #%d: %s"% (case_no, str(solution))
    case_no += 1
