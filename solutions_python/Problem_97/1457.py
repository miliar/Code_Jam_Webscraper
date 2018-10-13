import sys

def process(inputfile, outputfile):
    f = open(inputfile, 'r')
    inputdata = f.readlines()
    f.close()

    it = iter(inputdata)

    # number of cases
    N = int(it.next())
    
    fout = open(outputfile, 'w')

    for i in range(1, N+1):
        str1 = "Case #" + str(i) + ": "
        fout.write(str1)

        line = [int(digit) for digit in it.next().split()]
        
        n = line[0]
        m = line[1]

        i = 0
        l = []
        
        for n in range(n, m+1):
            n_str = str(n)
            n_next = n + 1
            for num in range(n_next, m+1):
		num1 = str(num)
		for j in range(-1, -len(n_str)-1, -1):
			t = n_str[j:] + n_str[:j]
			if t.startswith('0'):
                            continue
			t1 = int(t)
			if t1 == num and (n,num) not in l and (num,n) not in l:
				l.append((n,num))
				i += 1

        fout.write(str(i) + "\n")

    fout.close()
    
def main():
    if len(sys.argv) != 3:
        print 'usage: ./recycled.py inputfile outputfile'
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    process(inputfile, outputfile)

if __name__ == '__main__':
    main()
