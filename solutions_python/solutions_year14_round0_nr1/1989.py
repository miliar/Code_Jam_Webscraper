import sys
i = open("input.txt","r")
o = open("output.txt","w")

def main():
    
    nCases = int(i.readline())
    output = []
    for case in range(nCases):
        nrow = int(i.readline())
        row = []
        for no in range(4):
            row.append(map(int,i.readline().split()))
        

        prow = int(i.readline())
        pnrow = []
        for no in range(4):
            pnrow.append(map(int,i.readline().split()))
        count = 0
        list = []
        for numbers in row[nrow - 1]:
            for nextnumbers in pnrow[prow - 1]:
                if numbers == nextnumbers:
                    count+=1
                    list.append(numbers)
        if count == 0:
            output.append("Case #"+str(case+1)+": Volunteer cheated!")
     
        elif count == 1:
            output.append("Case #"+str(case+1)+": "+str(list[0]))
        else:
            output.append("Case #"+str(case+1)+": Bad magician!")

    for case in range(nCases):
        #print output[case]
        o.write("{0}\n".format(output[case]))

    

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
            pass     
    main()
    i.close()
    o.close()

