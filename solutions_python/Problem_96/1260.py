#!/usr/bin/python

def main ():
    output_file = 'output.txt'
    input_file = 'B-large.in'
    fout = open (output_file, 'w')
    c = 1
    with open(input_file, 'r') as fin:
        count = int(fin.readline())
        for line in fin:
            input_values = line.split()
            num_googlers = int (input_values.pop (0))
            surprisings = int (input_values.pop (0))
            win_score = int (input_values.pop (0))
            print num_googlers, surprisings, win_score
            no = []
            maybe = []
            yes = []
            winners = 0
            print '---------------------------------------------------------------'
            for value in input_values:
                value = int (value)
                mean = value / 3
                reminder = value % 3
                avail = min (2, (mean+reminder))
                #print 'value: %s, mean: %s, reminder: %s, avail: %s' %(value, mean, reminder, avail)
                if mean >= win_score or (mean + min(1, reminder)) >= win_score:
                    yes.append ((mean, reminder))
                elif mean < win_score and ((mean + reminder) >= win_score or (mean + min(1, avail) >= win_score)):
                    maybe.append ((mean, reminder))
                else:
                    no.append((mean, reminder))
            print yes, maybe, no
            while surprisings > 0:
                try:
                    combination = maybe.pop(0)
                except Exception, ex:
                    print ex
                    surprisings = 0
                else:
                    try:
                        yes.append(combination)
                    except Exception, ex:
                        print ex
                        surprisings = 0
                surprisings -= 1
                    
            print yes, maybe, no
            print len(yes)
                    
            fout.write('Case #%s: %s\n' %( c, len(yes)))
            c += 1
    fout.close()

if __name__ == '__main__':
    main ()

