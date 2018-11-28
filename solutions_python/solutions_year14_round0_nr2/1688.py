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

        sample = acc[i].split()
        sample = [float(n) for n in sample]

        samples.append(sample)

        
        
        i = i+1
    return samples


def oreil(file_name):
    file = read_file(file_name)

    output = open('oreil.txt', 'w')

    j = 0
    for sample in file:
        j += 1
        
        c = sample[0]
        f = sample[1]
        x = sample[2]

        o = x/2
        
        results = [o]


        i = 1
        
        
        while True:

            b = 0
            res = 0
            while b < i:
                res += c/(2+b*f)
                b += 1
                
            res += x/(2+(i)*f)

            results.append(res)
            i+=1

            if len(results) > 2:
                #print(i)
                good = (results[i-3] >= results[i-2] <= results[i-1])
            else:
                
                good = results[i-1] > results[0]

            if good:
                break

        res = round(min(results), 7)

        s = 'Case #%s: '%(j) + str(res) +'\n'
        output.write(s)

        
        
                

    
    


if __name__=='__main__':
    oreil('resB.txt')
