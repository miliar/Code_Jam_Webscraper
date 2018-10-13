def main(input_file):
    fh = open(input_file, "r")
    cases = fh.readline().strip()
    for count in xrange(1, int(cases) + 1):
        stats = fh.readline().strip().split(" ")
        c, f, x = [float(stats[0]), float(stats[1]), float(stats[2])]
        rate = 2
        cookies = 0
        total_time = 0
        done = False
        while not done:
            newrate = rate + f
            if  ((x-c)/rate) > (x/newrate):
                total_time += c/rate
                rate = newrate
                continue
            else:
                total_time += x/rate
                done = True
        
        
        print "Case #{0:}: {1:.7f}".format(count, total_time)
    #print entries
    fh.close()



if __name__ == "__main__":
    main("B-large.in")
