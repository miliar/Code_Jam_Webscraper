def Ovation(filename):
    input_file = open(filename, 'r')
    source = input_file.read()
    source = source.splitlines()
    input_file.close()
    output = open('output.txt', 'a')
    for i in range(int(source[0])):
        output.write('Case #%d: '%(i+1))
        total = 0
        friends = 0
        shymax, audience = source[i+1].split()
        for shyness in range(int(shymax)):
            total += int(audience[shyness])
            if total == shyness:
                friends += 1
                total += 1
        output.write(str(friends) + '\n')
    output.close()

Ovation('A-large.in')
