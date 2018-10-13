f = open('data1.txt')
w = open('out','w')
for case in range(int(f.readline())):
    row = int(f.readline())
    first = []
    for r in range(4):
        line = f.readline()
        if row == r + 1:
            first = line.strip()
            first = first.split()
    row = int(f.readline())
    second = []
    for r in range(4):
        line = f.readline()
        if row == r + 1:
            second = line.strip()
            second = second.split()
    match = 17
    matches = 0
    print(first, second)
    for num in first:
        if num in second:
            match = num
            matches += 1
            print(match)
    if match == 17:
        w.write('Case #' + str(case + 1) +': Volunteer cheated!\n')
    elif matches == 1:
        w.write('Case #' + str(case + 1) +': '+ str(match)+'\n')
    else:
        w.write('Case #' + str(case + 1) +': Bad magician!\n')
w.close()
            
