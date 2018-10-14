with open('A-large.in', 'r') as a:
    text = a.readlines()
    a.close()
b = open('A-large.out', 'w+')
cases = int(text[0])
for i in range(1, cases + 1):
    data = text[i].split()
    max_shyness = int(data[0])
    distr = data[1]
    num_friends = 0
    current_standing = 0
    for shyness, people in enumerate(distr):
        if shyness > current_standing:
            num_friends += shyness - current_standing
            current_standing += shyness - current_standing
        current_standing += int(people)
    b.write("Case #{}: {}\n".format(i, num_friends))
b.close()