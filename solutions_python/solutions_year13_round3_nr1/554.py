#!/usr/bin/env python3
import argparse
import itertools

parser = argparse.ArgumentParser(description="google code jam practice all your base")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")

vowels = "aeiou"

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        word, N = f.readline().split()
        N = int(N)
        yield word, N


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def count_consonats(s):
    return len([letter for letter in s if letter not in vowels])

def substrings(s, N):
    start = 0
    end = start+N
    while end < len(s)+1:
        yield s[start:end]
        start +=1
        end+=1



def main():
    for n, case in enumerate(read_input(), start=1):
        print(case)
        word, N = case

        outstring = count_consonats(word)
        # print(list(itertools.combinations(word, N)))
        # print(list(substrings(word, N)))

        number_of_matching_substrings = 0

        answer = 0
        # for ss in substrings(word, N):
        #     if len([i for i in ss if i in vowels]) == 0:
        #         answer += (len(word)-number_of_matching_substrings) - (N-1)
        #         number_of_matching_substrings += 1


        start = 0
        end = start+N
        counted_up_to = 0
        while end < len(word)+1:
            ss = word[start:end]
            letters_after = len(word)-end
            letters_before = start-counted_up_to
            # print(ss, letters_before, letters_after)
            if len([i for i in ss if i in vowels]) == 0:
                # print((1+letters_after),(letters_before+1))
                increment = (1+letters_after)*(letters_before+1)
                # print("adding", increment )
                answer += increment
                #*((len(word)-number_of_matching_substrings) - (N-1))
                number_of_matching_substrings += 1
                counted_up_to = start+1

            start += 1
            end += 1

        output(n, answer)



if __name__ == "__main__":
    main()
