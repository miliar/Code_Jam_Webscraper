


# Main

fout = open("output3.txt","wb")
with open("small_in3.txt") as fin:
    T = int(fin.readline());     # number of test cases
    for i in range(T):
        r, t = [int(x) for x in fin.readline().split()] # read first line

        n = 0;
        paint = 0;
        while paint <= t:

            n += 1;
            paint += ((r+((2*n)-1))**2) - ((r+((2*n)-2))**2);

        # Write to output
        output_str = "Case #" + str(i+1) + ": " + str(n-1) + "\n";
        fout.write(output_str)

fout.close()


