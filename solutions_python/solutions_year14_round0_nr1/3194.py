input_file = open('/Users/Aida/Desktop/googlecodejam/input_magic.txt')
output_file = open('/Users/Aida/Desktop/googlecodejam/output_magic.txt', 'w')

T = int(input_file.readline()) # number of test cases

i =1

d = {} # dictionary
row1 = []
row2 = []
entries = 0
entry = []

while i <= T:
    ans1 = 'a' + input_file.readline()
    d['a1\n'] = input_file.readline().split()
    d['a2\n'] = input_file.readline().split()
    d['a3\n'] = input_file.readline().split()
    d['a4\n'] = input_file.readline().split()
    ans2 = 'b' + input_file.readline()
    d['b1\n'] = input_file.readline().split()
    d['b2\n'] = input_file.readline().split()
    d['b3\n'] = input_file.readline().split()
    d['b4\n'] = input_file.readline().split()
    
    row1 = d[ans1]
    row2 = d[ans2]

    for e in row1:
        if e in row2:
            entries += 1
            entry.append(e)
    if entries == 0:
        output_file.write("Case #" + str(i) + ": Volunteer cheated!")
    if entries == 1:
        output_file.write("Case #" + str(i) + ": " + str(entry[0]))
    if entries > 1:
        output_file.write("Case #" + str(i) + ": Bad magician!")

    i +=1
    d = {}
    entries = 0
    entry = []

    if i<= T:
        output_file.write("\n")

input_file.close()
output_file.close()