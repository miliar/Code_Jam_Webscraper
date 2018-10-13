def tokenizer(stream):
    for line in stream:
        for token in line.split():
            yield token

filename = 'C-small-attempt1.in'

def main():
    with open(filename, 'r') as file_stream:
        tokenized = tokenizer(file_stream)
        T = int(next(tokenized))
        for case in range(T):
            N = int(next(tokenized))
            L = int(next(tokenized))
            H = int(next(tokenized))
            freqs = []
            for p in range(N):
                freqs.append(int(next(tokenized)))
            sol = False
            for f in range(L, H+1):
                for freq in freqs:
                    if freq%f == 0 or f%freq == 0:
                        continue
                    else:
                        break
                else:
                    print("Case #%d: %d"%(case+1, f))
                    break
            else:
                print("Case #%d: NO"%(case+1))

main()