# Problem A

##Problem
##
##Maria has been hired by the Ghastly Chemicals Junkies (GCJ) company to help them manufacture bullseyes. A bullseye consists of a number of concentric rings (rings that are centered at the same point), and it usually represents an archery target. GCJ is interested in manufacturing black-and-white bullseyes. 
##
##Maria starts with t millilitres of black paint, which she will use to draw rings of thickness 1cm (one centimetre). A ring of thickness 1cm is the space between two concentric circles whose radii differ by 1cm.
##
##Maria draws the first black ring around a white circle of radius r cm. Then she repeats the following process for as long as she has enough paint to do so:
##
##Maria imagines a white ring of thickness 1cm around the last black ring.
##Then she draws a new black ring of thickness 1cm around that white ring.
##Note that each "white ring" is simply the space between two black rings.
##The area of a disk with radius 1cm is π cm2. One millilitre of paint is required to cover area π cm2. What is the maximum number of black rings that Maria can draw? Please note that:
##
##Maria only draws complete rings. If the remaining paint is not enough to draw a complete black ring, she stops painting immediately.
##There will always be enough paint to draw at least one black ring.
##Input
##
##The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a line containing two space separated integers: r and t.
##
##Output
##
##For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the maximum number of black rings that Maria can draw.

def paint(num_rings, r):
    return(num_rings * (2 * num_rings + 2 * r - 1))

# Get input file
input_fname = input("Input filename: ")
infile = open(input_fname, 'r')
# Set output file
output_fname = input_fname.replace("in", "out")
outfile = open(output_fname, 'w')

N = int(infile.readline().strip("\n"))

for casenum in range(N):
    print("Case #", casenum+1, ": ", sep="", end="", file=outfile)

    r, t = [int(x) for x in infile.readline().strip("\n").split(" ")]
    k1 = int(((1 - 2*r) + pow((2*r-1)*(2*r-1) + 8*t, .5))/4)
    k2 = int(((1 - 2*r) - pow((2*r-1)*(2*r-1) + 8*t, .5))/4)

    if paint(k1, r) <= t and paint(k1 + 1, r) > t:
        print(k1, end="", file=outfile)
    elif paint(k1 - 1, r) <= t and paint(k1, r) > t:
        print(k1 - 1, end="", file=outfile)
    else:
        print(k2, end="", file=outfile)

    #print(k1, k2)
        
    print("", file=outfile)
# end case loop

infile.close()
outfile.close()
