def solve(row1, row2):
    cards = row1 & row2
    
    if len(cards) == 1:
        return str(cards.pop())
    
    if len(cards) < 1:
        return "Volunteer cheated!"
    
    if len(cards) > 1:
        return "Bad magician!"

f_in = open("in.txt")
f_out = open("out.txt","+w")
n_cases = int(f_in.readline())

print(str(n_cases) + " test cases!")

for case_nr in range(n_cases):
    
    r1 = int(f_in.readline())
    print(r1)
    
    for rowNo in range(r1-1):
        f_in.readline()
    row1 = {int(x) for x in f_in.readline().split(' ')}
    print(row1)
    
    for rowToEnd in range(4-r1):
        f_in.readline()

    r2 = int(f_in.readline())
    print(r2)
    
    for rowNo in range(r2-1):
        f_in.readline()
    row2 = {int(x) for x in f_in.readline().split(' ')}
    print(row2)
    
    
    for rowToEnd in range(4-r2):
        f_in.readline()
    
    ans = solve(row1, row2)
    print (ans)
    f_out.write("Case #" + str(case_nr+1) + ": " + ans + "\n")

f_in.close()
f_out.close()
