
import sys


if __name__ == '__main__':

    if len(sys.argv)> 1:
        file_name = sys.argv[1]
    else:
        file_name  = "A-large.in"

    filei = open(file_name)
    fileo = open(file_name + ".out", "w+")
    i = 1
    num_inputs = 0
    line = filei.readline()
    num_inputs = int(line)
    
    for line in filei:

        if i > 10000:
            break
        nk = line.split(" ")

        n = int(nk[0])
        k = int(nk[1])

        state = None
        if n != 0 and ((k+1) % (2**n)) == 0:
            state = "ON"
        else:
            state = "OFF"
        print >> fileo, "Case #%d: %s" % (i, state)

        i += 1
    fileo.flush()
    filei.close
    fileo.close
        

    
