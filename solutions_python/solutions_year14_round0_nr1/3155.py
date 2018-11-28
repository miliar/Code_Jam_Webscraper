import os

project_dir = os.path.dirname(os.path.realpath(__file__))

filename = 'q-a.1.txt'

in_path = os.path.join(project_dir, 'data', filename)
out_path = os.path.join(project_dir, 'output', filename)

with open(in_path) as in_file, open(out_path, 'w') as out_file:
    case_count = int(in_file.readline())

    for x in range(0, case_count):
        ans1 = int(in_file.readline())
        cards1 = []
        for _a in range(0, 4):
            cards1.append({int(a) for a in in_file.readline().split(' ')})

        ans2 = int(in_file.readline())
        cards2 = []
        for _b in range(0, 4):
            cards2.append({int(a) for a in in_file.readline().split(' ')})

        row1 = cards1[ans1 - 1]
        row2 = cards2[ans2 - 1]

        ans = row1 & row2

        if len(ans) == 1:
            out = ans.pop()
        elif len(ans) == 0:
            out = 'Volunteer cheated!'
        else:
            out = 'Bad magician!'

        output = 'Case #{}: {}'.format(x + 1, out)
        print(output)
        print(output, file=out_file)
