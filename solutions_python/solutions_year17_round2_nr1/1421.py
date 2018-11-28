# Open the given file 
lines = open("input.txt", "r").readlines()

# Save the number of test cases as an integer
t = int(lines.pop(0))

# Create a function to do the hard work
def speed(d, listy):
    """Returns the speed needed to cover the distance d without
    overtaking any of the horses in listy (pos, speed)"""
    
    times = [(d - listy[i][0]) / listy[i][1] for i in range(len(listy))]
    t = max(times)
    return d/t
        
# Create a file for the answer and line by line write the answer
outfile = open("answer.txt", "w")
for j in range(1,t+1):
    d, n = lines.pop(0).split()
    d, n = int(d), int(n)
    ps_list = []
    for i in range(n):
        p, s = lines.pop(0).split()
        p, s = int(p), int(s)
        ps_list.append((p,s))
    s = speed(d, ps_list)
    line = "Case #" + str(j) + ": " + str(s) + "\n"
    outfile.write(line)
outfile.close()
