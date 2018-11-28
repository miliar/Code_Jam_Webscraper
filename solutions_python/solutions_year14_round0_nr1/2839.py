f = open("input.txt", "rU")
cases = int(f.readline().strip())
results = ""
for case in range(cases):
    line_number = int(f.readline().strip())
    for i in range(4):
        line = f.readline().strip()
        if i+1 == line_number:
            line1 = line.split()
    line_number = int(f.readline().strip())
    for i in range(4):
        line = f.readline().strip()
        if i+1 == line_number:
            line2 = line.split()
            count = 0
            for item in line1:
                if item in line2:
                    count += 1
                    result = item
            if count == 0:
                results += "Case #{}: Volunteer cheated!\n".format(case+1)
            elif count == 1:
                results += "Case #{}: {}\n".format(case+1, result)
            else:
                results += "Case #{}: Bad magician!\n".format(case+1)
f.close()
results = results.strip()

o = open("output.txt", "w")
o.write(results)
o.close()
