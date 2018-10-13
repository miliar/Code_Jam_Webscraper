"""
Jonathan Simowitz

Google Code Jam 2012
Qualification Round
"""

import os

def get_recycles(data):
    item = data.pop(0)
    text = str(item)
    matches = 1
    for i in range(1,len(text)):
        rec_text = text[i:] + text[:i]
        rec_int = int(rec_text)
        if rec_int in data:
            data.remove(rec_int)
            matches += 1
    rec = (matches+1)*matches/2 - matches
    if data:
        return rec + get_recycles(data)
    else:
        return rec

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data):
    data = data.split()
    A = int(data[0])
    B = int(data[1])
    storage = {}
    recycles = 0
    for n in range(A,B+1):
        key = list(str(n))
        key.sort()
        key = str(key)
        try:
            storage[key].append(n)
        except:
            storage[key] = [n]
        """
        Brute force method... too slow
        for m in range(n+1,B+1):
            lst_n = list(str(n))
            lst_m = list(str(m))
            if set(lst_n) != set(lst_m):
                continue
            for i in range(len(lst_n)):
                lst_n.append(lst_n.pop(0))
                if lst_n == lst_m:
                    recycles += 1
                    break
        """
    for k,v in storage.iteritems():
        recycles += get_recycles(v)
        
    return str(recycles)

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "C-small-attempt0.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    heading = True
    test_num = 1

    #Iterate through the input file
    while True:
        #read input one line at a time
        line = rf.readline()
        line = line.strip()

        if not line:
            #end of file

            #close input file
            rf.close()
            #close output file
            wf.close()
            break
        else:
            #process the line

            if (heading):
                heading = False
                NUM_TEST_CASES = int(line)
            else:
                #print the output
                wf.write("Case #" + str(test_num) + ": " + process(line) + "\n")
                #increment the test case number
                test_num += 1

main()
