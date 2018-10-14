#!/usr/bin/python
import sys, getopt

def write_in_file(text,filename):
    with open(filename,"w") as f:
        f.write(text)

def read_input(filename):
    file = open(filename,'r') 
    return [int(numb) for numb in file.readlines()[1:]] 

def checkTeddy(number):
    arr = list(str(number))
    for i in range(0,len(arr)-1):
        if int(arr[i])>int(arr[i+1]):
            number_to_substract = int(''.join(arr[i+1:]))+1
            return [False,number_to_substract]
    return [True,number]

def find_last_teddy_number(numb):
    teddyCheck = checkTeddy(numb)
    while not teddyCheck[0]:
        print(numb)
        numb-=teddyCheck[1]
        teddyCheck = checkTeddy(numb)
    return numb


def find_all_teddies(numb_array):
    res = []
    for i in range(0,len(numb_array)):
        res.append('Case #{}: {}'.format(i+1,find_last_teddy_number(numb_array[i])))
    return res

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'teddy.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    print 'Input file is :', inputfile
    print 'Output file is :', str(read_input(inputfile))
    write_in_file('\n'.join(find_all_teddies(read_input(inputfile))),outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])

# print(find_all_teddies([132,1000,7,111111111111111110]))
# print(find_last_teddy_number(111111111111111110))