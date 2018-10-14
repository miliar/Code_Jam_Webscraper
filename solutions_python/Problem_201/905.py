import sys



def split_sequence(n):
    if n%2:
        return (n-1)/2, (n-1)/2
    return n/2-1, n/2


if __name__ == "__main__":
    filename = sys.argv[1]
    infile = open(filename+".in", "r")
    outfile = open(filename+".out", "w")
    T = int(infile.readline())
    for case in range(T):
        N, K = [int(char) for char in infile.readline().split()]
        remaining_people = K
        coming_people = 1
        while remaining_people - coming_people >= 0:
            remaining_people -= coming_people
            coming_people *= 2
        length = float(N-K)/float(coming_people//2)
        if remaining_people > 0:
            length /= 2.0
        min_free = int(length/2)
        max_free = int(length-min_free)
        #print max_free, min_free
        outfile.write("Case #{}: {} {}\n".format(case+1, max_free, min_free))
    infile.close()
    outfile.close()
