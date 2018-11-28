def main(filename):
    inputfile = open(filename+".in","r")
    outputfile = open(filename+".out", "w")

    T = int(inputfile.readline().strip())
    for i in range(T):
        tmp = inputfile.readline().strip()
        R, K, N = [int(n) for n in tmp.split()]

        tmp = inputfile.readline().strip()
        groups = [int(n) for n in tmp.split()]

        count = 0
        for j in range(R):
            boarded = []
            while 1:
                if (len(groups)==0 or groups[0]+sum(boarded)>K):
                    break
                else:
                    boarded.append(groups.pop(0))
            groups.extend(boarded)
            count += sum(boarded)
        output = "Case #%d: %d\n" % (i+1, count)
        outputfile.write(output)

    inputfile.close()
    outputfile.close()

if __name__ == "__main__":
    main("sample")
