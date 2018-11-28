def check_power(n):
    if sum(snappers[:n]) == len(snappers[:n]):
        status = "ON"
    else:
        status = "OFF"
    return status

def switch(n):
    if check_power(n) == "ON":
        if snappers[n] == 0:
            snappers[n] = 1
        else:
            snappers[n] = 0

def fingers(snapper_num, n):
    global snappers
    snappers = [0] * snapper_num
    for i in range(n):
        for j in range(len(snappers)-1, -1, -1):
            switch(j)

    return check_power(n+1)

def main(fili, filo):
    inputfile = open(fili,"r")
    outputfile = open(filo,"w")

    T = int(inputfile.readline().strip())
    for i in range(T):
        tmp = inputfile.readline().strip()
        N, K = tmp.split()
        N, K = int(N), int(K)
        output = "Case #%d: %s\n" % (i+1, fingers(N, K))
        outputfile.write(output)

    outputfile.close()
    inputfile.close()

if __name__ == "__main__":
    main("A-small-attempt0.in", "A-small-attempt0.out")
