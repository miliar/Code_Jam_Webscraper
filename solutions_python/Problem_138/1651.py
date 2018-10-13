import copy

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
    
    dim = acc[0]
    while acc[i]:
        

        pla1 = acc[i+1].split()
        pla2= acc[i+2].split()

        pla1 = [float(x) for x in pla1]
        pla2 = [float(x) for x in pla2]


        

        sample = {'p1':pla1, 'p2': pla2}

        samples.append(sample)

        
        
        i = i+3

    return samples


def play_war(sam):
    sample = copy.deepcopy(sam)
    pla1 = sample['p1']
    pla2 = sample['p2']

    pla1.sort()
    pla2.sort()


    score = 0
    for x in (pla1):

        
        i = 0
        c = 0
        while i < len(pla2):
            if pla2[i] > x:
                c = pla2.pop(i)
                break
            i += 1
            
        if not c:
            score += 1
        
            
    return(score)
    

def play_dwar(sam):
    sample = copy.deepcopy(sam)
    pla1 = sample['p1']
    pla2 = sample['p2']

    pla1.sort()
    pla2.sort()

    while True:
        m = max(pla2) if pla2 else 0

        if all(m > x for x in pla1) and pla2:
            
            pla2 = pla2[:len(pla2)-1]
            pla1 = pla1[1:]
            
        else:
            break

    score = 0

    pla2.sort(reverse=True)
    for x in (pla2):
        i = 0
        c = 0
        while i < len(pla1):
            if pla1[i] > x:
                c = pla1.pop(i)
                score += 1
                break
            i += 1
            


    return score
        

def main(file_name):
    file = read_file(file_name)

    output = open('war_res_big.txt', 'w')

    i= 0 
    for s in file:
        w = play_war(s)
        d = play_dwar(s)
        
        i += 1
        s = 'Case #%s: '%(i) + str(d) +' ' + str(w) +'\n'
        output.write(s)




if __name__=='__main__':
    main('war_big.txt')
    print('all')

