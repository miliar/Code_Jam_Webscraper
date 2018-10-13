# Magic Trick
# https://code.google.com/codejam/contest/2974486/dashboard
# Qual Round 2014 6 pts

import sys

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    
    line = infile.readline()
    T = int(line)

    for t in range(1,T+1):
        line = infile.readline()
        r1 = int(line)

        for i in range(1,5):
            line = infile.readline()
            if i==r1:
                row1 = line.strip('\n').split(" ")

        print (row1)
        line = infile.readline()
        r2 = int(line)

        for i in range(1,5):
            line = infile.readline()
            if i==r2:
                row2 = line.strip('\n').split(" ")

        print (row2)

        count = 0
        for i in range(0,4):
            if row2[i] in row1:
                if count == 0:
                    result = row2[i]
                    count +=1
                else:
                    count += 1
                    outfile.write("Case #{0}: Bad magician!\n".format(t))
                    print("Case #{0}: Bad magician!\n".format(t))
                    break
        if count == 0:
            outfile.write("Case #{0}: Volunteer cheated!\n".format(t))
            print("Case #{0}: Volunteer cheated!\n".format(t))
        elif count == 1:
            outfile.write("Case #{0}: {1}\n".format(t, result))
            print("Case #{0}: {1}\n".format(t, result))
    
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
    
        
    
        
    
