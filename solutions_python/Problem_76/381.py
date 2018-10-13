'''
Created on 7-may-2011

@author: Joachim Van Herwegen
'''

def parse_input():
    input = []
    
    file = open("candy_splitting_large.txt", 'rU')
    file.readline()
    while file.readline():
        line = file.readline()
        input.append([int(x) for x in line.split()])
    return input

def split_possible(input):
    result = 0
    for val in input:
        result ^= val
    return not result

def calc_result(input):
    if not split_possible(input):
        return 'NO'
    if not len(input):
        return 0
    sorted_input = sorted(input)
    return sum(sorted_input[1:])

def main():
    results = []
    for input in parse_input():
        results.append(calc_result(input))
        
    output = open("output_candy_splitting_large.txt", 'w')
    for i, result in enumerate(results):
        output.write("Case #%d: %s" % (i+1, str(result)))
        if i < len(results)-1:
            output.write("\n")
    output.close()

if __name__ == "__main__":
    main()