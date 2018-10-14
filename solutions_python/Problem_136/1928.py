import sys
inp = open("inp3.txt","r")
out = open("new2.txt","w")

def main():
    
    nCases = int(inp.readline())
    output = []
    for case in range(nCases):
        row = map(float,inp.readline().split())
        time = []
        #row.append(map(float,sys.stdin.readline().split()))
        #print row
        #c = row[0]
        #f = row [1]
        #x = row[2]

        rn = int(row[2] / row[0])
        
        for n in range(rn + 2):
            sum = 0
            if n == 0:
                sum = (row[2]/2)
            else:
                for i in range(n):
                    sum = sum + (row[0]/(2 + i*row[1]))
                sum = sum +(row[2]/ (2 + ((n)*row[1])))
            time.append(sum)

        i = 0
        while (time[i+1] < time[i]):
            i = i + 1
        min = time[i]
        output.append("Case #"+str(case+1)+": "+str('%.7f'%min))

    for case in range(nCases):
        #print output[case]
        out.write("{0}\n".format(output[case]))

        

    

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
            pass     
    main()
    inp.close()
    out.close()
