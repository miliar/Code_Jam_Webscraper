import sys, re


output_line = "Case #{case_number:d}: {word_count:d}"

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
        L, D, N = map(int, infile.readline().split())
        words = []
        for d in range(D):
            words.append(infile.readline().strip(" \n\r"))
        for n in range(N):
            pattern = infile.readline().strip(" \n\r")
            pattern = re.sub("\(", "[", pattern)
            pattern = re.sub("\)", "]", pattern)
            pattern = re.compile(pattern)
            word_count = sum(1 if pattern.match(word) else 0 for word in words)
            print(output_line.format(case_number=n+1, word_count=word_count), file=outfile)
