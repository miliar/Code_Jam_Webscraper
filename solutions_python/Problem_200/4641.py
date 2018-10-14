def main():
    inputfile = open("B-small-attempt0.in", "r")
    f = open("small_output.txt", "w")
    filecontent = inputfile.read().splitlines()
    cases = int(filecontent[0])
    for x in range(1,cases+1):
        num = int(filecontent[x])
        while(num):
            var = num
            reminder = []
            while(var>9):
                reminder.append(var%10)
                var = int(var/10)
            reminder.append(var)
            tmplst = sorted(reminder,reverse=True)
            if(tmplst==reminder):
                printval = ("Case #"+str(x)+": "+str(num))
                f.write(printval)
                f.write("\n")
                break
            num-=1
    f.close()


if __name__ == '__main__':
    main()