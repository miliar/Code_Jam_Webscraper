#$$
def getParticles(line):
    particles = []
    t = []
    for item in line:
        if item == '(':
            if t:
                particles.append("".join(t))
                t = []
            continue
        if item == ')':
            if t:
                particles.append(t)
                t = []
            continue
        t.append(item)
    particles.append("".join(t))
    return particles

fileName = 'A-large.in'
#fileName = 'A-small-practice.in'
data_file = open(fileName,'r')

data = data_file.readlines()

header = data[0].strip()

L,D,N = map(int,header.split(' '))

if (L > 15 or L < 1):
    exit()
if (D > 5000 or D < 1):
    exit()
    
if (N > 500 or N < 1):
    exit()

alien_words = [x.strip() for x in data[1:D+1]]

data_file.close()

fileOut = 'A-large.out'

data_file = open(fileOut,'a')


f = 1
for line in data[D+1:]:
    total = 0
    line = line.strip()
    line = line.split()[0]
    cases = []
    particles = getParticles(line)

    #if len(particles) > 1:
    for particle in particles:
    #    sylab = []
        if particle != '':
            cases.append(particle)
    
    #print cases
    
    flag = True

    if len(particles)> 1:
        for word in alien_words:
            index = 0
            for element in cases:
                if type(element) == list:
                    if word[index] not in element:
                        flag = False
                        break
                    index+=1
                elif type(element) == str:
                    print element
                    size = len(element)
                    if word[index:index+size] != element:
                        flag = False
                        break
                    index+=size
            if flag:
                total+=1
            flag = True
    else:
        total =  alien_words.count(particles[0])
        
    out = 'Case #%d: %s\n' %(f,total)
    data_file.write(out)
    f+=1

