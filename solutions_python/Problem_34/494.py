#google code jam '09 template
#
import re

file_name = 'A-large.in'
read_fp = None

def main():
    global read_fp
    Initializations()

    dictionary = []

    [l, d, n] = read_fp.readline().strip().split(' ')

    l = int(l)
    d = int(d)
    n = int(n)
    
    for i in range(d):
        dictionary += [read_fp.readline().strip()]

    for i in range(n):
        word = read_fp.readline().strip()
        count = 0
        pattern = re.compile(word.replace('(','[').replace(')',']'))
        for j in dictionary:
            if pattern.match(j):
                count += 1

        print "Case #%i:"%(i+1),count
    


    read_fp.close()
    return














def Initializations():
    global file_name
    global read_fp
    read_fp = open(file_name, 'r')
    return

if (__name__ == "__main__"):
    main()
