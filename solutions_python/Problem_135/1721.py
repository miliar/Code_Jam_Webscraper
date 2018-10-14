def read_file(file_name):
    file = open(file_name, 'r')

    cr = 'q'
    acc = []
    
    while cr != '':
        cr = file.readline()
        acc.append(cr)

    num_of_samples = int((acc.pop(0)))

    samples = []

    i = 0
    while acc[i]:
        answer1 = int(acc[i])

        
        
        
        perm1 = acc[i+1:i+5]

        perm1 = [x.split() for x in perm1]


        
        answer2 = int(acc[i+5])

        perm2 = acc[i+6:i+10]
        
        perm2 = [x.split() for x in perm2]

        sample = {'a1':answer1, 'a2':answer2, 'p1':perm1, 'p2':perm2}

        samples.append(sample)

        
        
        i = i+10
    return samples

def make_some_magic(file_name):
    file = read_file(file_name)

    output = open('magic.txt', 'w')

    i = 0
    for sample in file:
        i+=1
        numbers = []
        result = ''
        
        for a in sample['p1'][sample['a1']-1]:
            for b in sample['p2'][sample['a2']-1]:
                if int(a) == int(b):
                    numbers.append(a)
                    
        if not len(numbers):
            result = 'Volunteer cheated!'
            
        elif len(numbers) > 1:
            result = 'Bad magician!'

        elif len(numbers) == 1:
            result = numbers[0]

        s = 'Case #%s: '%(i) + str(result) +'\n'
        output.write(s)

        

