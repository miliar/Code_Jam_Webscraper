import sys

def goro_sort(array):
    sorted_array = sorted(array)
    in_place = 0
    for n in range(len(sorted_array)):
        if sorted_array[n] == array[n]: in_place += 1
    return str(len(array) - in_place) + '.000000'

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(int(Input[0])):
        array = Input[2*i + 2].split(' ')
        array = [int(n) for n in array]
        result = goro_sort(array)
        Output += "Case #" + str(i + 1) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__":
    main(sys.argv[1])
