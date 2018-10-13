
def main():
    f = open("input.txt", "r")
    f2 = open("output.txt", "r")
    num_test = int(f.readline())

    rest = f.readlines()
    sample = f2.readlines()

    if num_test != len(rest):
        print "ERROR: inconsistent problem state"
    rest = [s.strip() for s in rest]
    sample = [s.strip() for s in sample]


    cm = {}
    cm['z'] = 'q'
    cm['q'] = 'z'

    for line_num in range(len(rest)):
      for pos in range(len(rest[line_num])):
          cm[rest[line_num][pos]] = sample[line_num][pos]


    fp = open("problem1.txt", "r")
    n_t = int(fp.readline())
    prob = fp.readlines()
    prob = [s.strip() for s in prob]
    
    output = ""
    count = 1

    for line in prob:
        output += "Case #" +str(count)+": "
        for letter in line:
            if letter in cm:
                output += cm[letter]
            else:
                output += letter

        if count != len(prob):
            output += "\n"

        count += 1
        

    f_o = open("answer_sit.txt", "w")
    f_o.write(output)
            
    

    

if __name__ == "__main__":
    main()
