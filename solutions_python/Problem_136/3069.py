import os
import sys

project_dir = os.path.dirname(os.path.realpath(__file__))

filename = 'q-b.1.txt'

in_path = os.path.join(project_dir, 'data', filename)
out_path = os.path.join(project_dir, 'output', filename)

if len(sys.argv) == 2:
    in_path = sys.argv[1]
    out_path = os.path.join(project_dir, 'output', os.path.splitext(os.path.basename(in_path))[0] + '.out')

with open(in_path) as in_file, open(out_path, 'w+') as out_file:
    case_count = int(in_file.readline())

    for i in range(0, case_count):
        time = 0.0
        r = 2.0
        c, f, x = map(float, in_file.readline().split(' '))

        while True:
            time_to_build = c / r
            time_to_win_with_upgrade = time + time_to_build + (x / (r + f))
            time_to_win = time + x / r

            if time_to_win_with_upgrade < time_to_win:
                r += f
                time += time_to_build
            else:
                time = time_to_win
                break

        output = 'Case #{}: {:.7f}'.format(i + 1, time)
        print(output)
        print(output, file=out_file)
