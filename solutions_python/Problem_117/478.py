def status(lines):
    max_lines=tuple(max(line) for line in lines)
    max_rows=tuple(max(row) for row in zip(*lines))
    for i, mline in enumerate(max_lines):
        for j, mrow in enumerate(max_rows):
            if min(mline, mrow)>lines[i][j]:
                return "NO"
    return "YES"

file=open(r"C:\Users\user\Downloads\B-large.in").read().split('\n',1)[1]
file=tuple(tuple(int(i) for i in line.split(' ')) for line in file.splitlines())

i=1
while file:
    lines=file[1:1+file[0][0]]
    print("Case #"+str(i)+":", status(lines))
    file=file[1+file[0][0]:]
    i+=1
