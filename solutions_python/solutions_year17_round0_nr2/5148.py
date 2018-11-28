import sys

with open(sys.argv[1],'r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

t = lines.pop(0)
case = 1
untidy = []
for idx, line in enumerate(lines):
    s = sorted(line)
    s = int(''.join(s))
    untidy.append(str(''.join(line)))
    while True:
        tidy = "".join(sorted(str(untidy[idx])))
        if str(untidy[idx]) == str(tidy):
            print("Case #{}: {}").format(case,untidy[idx])
            break
        if untidy[idx] < 1:
            break
        else:
            untidy[idx] = int(untidy[idx]) - 1

    case += 1

