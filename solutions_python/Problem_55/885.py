# Google Code Jam - 2010
# B. Theme Park

class rc(object):
    def __init__(self, R, k, t):
        self.r = int(R) # no. of rounds/ total rides
        self.k = int(k )# capacity
        self.q = t # queue


    def rotate(self):
        """ rotates sequence in left by one place/
        decreases the index of each character by one """
        sequence = self.q
        t = []
        for i in range(len(sequence)-1):
            t.append(sequence[i+1])
                       
        t.append(sequence[0])
        self.q = t

    def income(self):
        i = 1
        income = 0
        max_rotation = len(self.q)
        while i <= self.r:
            c = 0 # current no. of people on board
            rotation = 0
            while c + int(self.q[0]) <= self.k and rotation < max_rotation:
                c += int(self.q[0])
                self.rotate()
                rotation += 1
            income += c
            i += 1  
        return income


fin = open('C-small-attempt0.in')
fout = open('B-small-output.txt', 'w')

total = []
for line in fin:
    a = line.strip()
    b = a.split(' ')
    total.append(b)

case_counter = 0
i = 1
while i+1 < len(total):
    case_counter += 1
    a = total[i]
    b = total[i+1]
    r = rc(a[0], a[1], b)
##    print r.r, r.k, r.q
    ans = r.income()
##    print r.income()
    ans_format = 'Case #%(c)i: %(ans)s' % \
              {'c':case_counter, 'ans': ans}
    fout.write(ans_format+'\n')
    i += 2
    
fout.flush()
fout.close()
fin.close()
