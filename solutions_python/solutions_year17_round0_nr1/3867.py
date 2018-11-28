#opf.py
import cjfile

class OPFFile(cjfile.CJFile):
    def next(self):
        super(OPFFile,self).next()
        line = self.next_line().split(' ')
        return line[0], int(line[1])

def output(number, answer):
    return 'Case #'+str(number)+': '+str(answer) + '\n'

def opf():
    file = OPFFile('A-large.in')
    outfile = open('A-large.out','wn')
    case_no = 0
    for panstr, flipk in file:
        case_no += 1
        flip_count = 0
        pan = []
        for val in panstr:
            if val=='-':
                pan.append(False)
            if val=='+':
                pan.append(True)
        while True:
            #print pan
            if len(pan) == flipk:
                if pan == [False]*flipk:
                    outfile.write(output(case_no,flip_count+1))
                    break
                elif pan == [True]*flipk:
                    outfile.write(output(case_no,flip_count))
                    break
                else:
                    outfile.write(output(case_no,'IMPOSSIBLE'))
                    break
            if pan.pop() == False:
                flip_count += 1
                for i in range(len(pan)+1-flipk,len(pan)):
                    pan[i] = not pan[i]
