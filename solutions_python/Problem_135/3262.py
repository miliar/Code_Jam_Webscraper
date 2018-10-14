import os


def solve(f):
    valA = int(f.readline())
    for i in range(1,5):
        if i == valA:
            rowA = f.readline()
        else:
            f.readline()
    valB = int(f.readline())
    for i in range(1,5):
        if i == valB:
            rowB = f.readline()
        else:
            f.readline()
    listA = rowA.split()
    listB = rowB.split()
    out = set(listA).intersection(listB)
    if len(out) == 1:
        return out.pop()
    elif len(out) == 0:
        return 'Volunteer cheated!'
    else:
        return "Bad magician!"
    


if __name__ == "__main__":
    input_filename = 'A-small-attempt0.in'
    output_filename = 'sampleout_0.txt'
 
    f_in = open(input_filename)
    counter = int(output_filename.split('.')[0][-1])
    while os.path.isfile(output_filename):
        counter += 1
        output_filename = output_filename.split(str(counter - 1) + '.')[0] + str(counter) + '.txt'
    f_out = open(output_filename, 'a')
 
    test_cases = int(f_in.readline())
    for i in range(test_cases):
        ans = solve(f_in)
        f_out.write('Case #' + str(i + 1) +': ' + str(ans) + '\n')
 
    f_in.close()
    f_out.close()
