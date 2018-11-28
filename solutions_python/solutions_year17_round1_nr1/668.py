import re


class Cake():
    def __init__(self, r, c):   
        self.cake = []
        self.r = r
        self.c = c

    def insert_r(self, row):
        self.cake.append(row)

    def get(self):
        return self.cake

    def make(self):
        new_cake = []

        for dummy_r in xrange(0,r):
            found_flag = False
            if re.match('^\?*$',self.cake[dummy_r]):
                for dummy_r_2 in xrange(dummy_r,r):
                    if not re.match('^\?*$',self.cake[dummy_r_2]):
                        new_cake.append(self.cake[dummy_r_2])
                        found_flag = True
                        break
                if not found_flag:
                    for dummy_r_2 in xrange(0, dummy_r + 1):
                        if not re.match('^\?*$',self.cake[dummy_r - dummy_r_2]):
                            new_cake.append(self.cake[dummy_r - dummy_r_2])
                            break
            else:
                new_cake.append(self.cake[dummy_r]) 

        self.cake = new_cake
        new_cake = []

        for dummy_r in xrange(0,r):
            row = ""
            pass_num = 0
            previous_letter = '?'

            for dummy_c in xrange(0,c):
                letter = self.cake[dummy_r][dummy_c]
                if letter != '?' and dummy_c != 0 and pass_num > 0:
                    for dummy_idx in xrange(0,pass_num + 1):
                        row += letter
                    pass_num = 0
                    previous_letter = letter
                elif letter == '?' and previous_letter != '?':
                    row += previous_letter
                elif letter == '?':
                    pass_num += 1
                else:
                    row += letter
                    previous_letter = letter
            new_cake.append(row)
        self.cake = new_cake
            
case = 0

read_file = open('large.in', 'r')
write_file = open('result.txt.large', 'w')

first_line = True
count = 0


for line in read_file:
    if first_line:
        first_line = False
        t = int(line.strip())
    else:
        line = line.strip()
        if count == 0:
            r, c = line.split()
            r = int(r)
            c = int(c)
            cake = Cake(r, c)
            count += 1
        elif count < r:
            cake.insert_r(line)
            count += 1
        else:
            cake.insert_r(line)
            cake.make()
            count = 0
            case += 1
            write_file.write("Case #" + str(case) + ':\n')
            for line in cake.get():
                write_file.write(line + '\n')