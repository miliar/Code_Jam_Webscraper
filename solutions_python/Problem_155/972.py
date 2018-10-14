def main():
    f = open('A-large.in', 'r')
    numberOfProblems = int(f.readline())
    out = open('A-large.out','w')
    for x in range(0,numberOfProblems):
        #solve the test case
        #single line per case
        lineIn = f.readline()
        smax,shyCount = lineIn.split(" ")
        shyCount = shyCount.replace("\n", "")
        smax = int(smax)
        count = 0
        totalStanding = int(shyCount[0])
        shyCount = shyCount[1:]
        needStanding = 1
        for i in shyCount:
            numShyGuy = int(i)
            while(needStanding > totalStanding):
                totalStanding += 1
                count += 1
            totalStanding += numShyGuy
                
            needStanding += 1
        

        #write answer to out
        out.write("Case #" + str(x+1) + ": " + str(count) + "\n")

    f.close()
    out.close()
        


if __name__ == "__main__":
    main()
