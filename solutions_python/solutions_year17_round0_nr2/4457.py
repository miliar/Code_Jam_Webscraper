def calculate_tidy_number(number):
    tidy_number = 0
    for j in xrange(number,0,-1):
        temp_number = j
        array_numbers = [int(d) for d in str(temp_number)]
        boo = all(array_numbers[i] <= array_numbers[i+1] for i in xrange(len(array_numbers)-1))
        if boo:
            tidy_number = j
            break
    return tidy_number

with open("/Users/smahimkar/Downloads/B-small-attempt0.in", "r") as inp, open("/Users/smahimkar/Downloads/B-small-attempt0.out", "w") as out:
    no_of_cases = int(inp.readline().strip())
    i=0
    for line in inp:
        i+=1
        number = int(line.strip())
        to_file = "Case #{}: {}\n".format(i, calculate_tidy_number(number))
        out.write(to_file)

