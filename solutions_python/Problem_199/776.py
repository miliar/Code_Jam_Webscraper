
import sys

def main():

    fin_name = sys.argv[1]
    fout_name = sys.argv[2]

    fout = open(fout_name, 'w')

    with open(fin_name, 'r') as fin:
        lines = fin.readlines()

    T = int(lines[0].split()[0])

    for test_case in range(1, T+1):
        string, k_flip = lines[test_case].split()
        k_flip = int(k_flip)

        flips = how_many_flips(string, k_flip)

        if flips >= 0:
            fout.write("Case #"+str(test_case)+": "+str(flips)+"\n")
        else:
            fout.write("Case #"+str(test_case)+": IMPOSSIBLE\n")



def how_many_flips(string, k_flip):

    flips = 0
    bin_array = [0 if sign == '-' else 1 for sign in string]

    for index in range (len(string)-k_flip+1):
        if bin_array[index] == 0:
            bin_array[index:index+k_flip] = [ (x+1)%2 for x in bin_array[index:index+k_flip]]
            flips += 1

    if sum(bin_array) != len(bin_array):
        return -1
    else:
        return flips

if __name__ == "__main__":
    main()
