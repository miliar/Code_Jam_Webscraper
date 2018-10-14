import sys,os

filename = sys.argv[1].strip()

ifile = open(filename + '.in','r')
all = ifile.readlines()
ifile.close()

ofile = open(filename + '.out','w')

num_lines = int(all[0])

letters = [ 'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m' ]

p = 0
for line in all[1:]:
    print line
    line = line[:-1].lower()
    possibles = [ [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[] ]
    n = 0
    while (n < len(letters)):
        try:
            m = min(possibles[n-1])
        except:
            m = 0
        while (m < len(line)):
            if (letters[n]==line[m]):
                possibles[n].append(m)
            m = m + 1
        n = n + 1

    counter = 0
    for num0 in possibles[0]:
        for num1 in possibles[1]:
            if (num1 > num0):
                for num2 in possibles[2]:
                    if (num2 > num1):
                        for num3 in possibles[3]:
                            if (num3 > num2):
                                for num4 in possibles[4]:
                                    if (num4 > num3):
                                        for num5 in possibles[5]:
                                            if (num5 > num4):
                                                for num6 in possibles[6]:
                                                    if (num6 > num5):
                                                        for num7 in possibles[7]:
                                                            if (num7 > num6):
                                                                for num8 in possibles[8]:
                                                                    if (num8 > num7):
                                                                        for num9 in possibles[9]:
                                                                            if (num9 > num8):
                                                                                for num10 in possibles[10]:
                                                                                    if (num10 > num9):
                                                                                        for num11 in possibles[11]:
                                                                                            if (num11 > num10):
                                                                                                for num12 in possibles[12]:
                                                                                                    if (num12 > num11):
                                                                                                        for num13 in possibles[13]:
                                                                                                            if (num13 > num12):
                                                                                                                for num14 in possibles[14]:
                                                                                                                    if (num14 > num13):
                                                                                                                        for num15 in possibles[15]:
                                                                                                                            if (num15 > num14):
                                                                                                                                for num16 in possibles[16]:
                                                                                                                                    if (num16 > num15):
                                                                                                                                        for num17 in possibles[17]:
                                                                                                                                            if (num17 > num16):
                                                                                                                                                for num18 in possibles[18]:
                                                                                                                                                    if (num18 > num17):
                                                                                                                                                        counter = counter + 1

    counter_last4 = str(counter)[-4:].zfill(4)
    print 'Case #%i: %4s' % (p+1,counter_last4)
    ofile.write('Case #%i: %4s\n' % (p+1,counter_last4))
    p = p + 1
    
