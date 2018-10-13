i = 0
t = 0
x = 0
def converting_numbers(my_list):
    z = []
    for word in my_list:
        z.append(int(word))
    return z

def comparing_numbers(a, b):
    z = list(set(a).intersection(b))
    if len(z) == 1:
        return str(z[0])
    elif len(z) > 1:
        c = "Bad magician!"
        return c
    elif len(z) < 1:
        c = "Volunteer cheated!"
        return c
        
with open('test1.out', 'w') as out_file:
    for line in open('A-small-attempt0.in'):
            i = i + 1
            if i == 2:
                x = int(line)
                t = t + 1
            elif i == 3 and x == 1:
                inputs = line.split()
                z = converting_numbers(inputs)
            elif i == 4 and x == 2:
                inputs = line.split()
                z = converting_numbers(inputs)
            elif i == 5 and x == 3:
                inputs = line.split()
                z = converting_numbers(inputs)
            elif i == 6 and x == 4:
                inputs = line.split()
                z = converting_numbers(inputs)
            elif i == 7:
                x = int(line)
            elif i == 8 and x == 1:
                inputs = line.split()
                z1 = converting_numbers(inputs)
                ans = comparing_numbers(z, z1)
            elif i == 9 and x == 2:
                inputs = line.split()
                z1 = converting_numbers(inputs)
                ans = comparing_numbers(z, z1)
            elif i == 10 and x == 3:
                inputs = line.split()
                z1 = converting_numbers(inputs)
                ans = comparing_numbers(z, z1)
            elif i == 11 and x == 4:
                inputs = line.split()
                z1 = converting_numbers(inputs)
                ans = comparing_numbers(z, z1)
            elif i == 1:
                m = int(line)
            if i == 11:
                i = 1
                statement = "Case #" + str(t) + ": " + ans
                out_file.write("%s\n" % statement)