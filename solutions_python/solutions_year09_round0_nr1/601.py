import re

def solve(input):
    L, D, N = [int(d) for d in input[0].split(" ")]
    words, testcases = input[1:1+D], [re.compile(l.replace('(','[').replace(')',']')) 
                                      for l in input[1+D:1+D+N]]
    joined_words = " ".join(words)
    result = ""
    
    for idx, test in enumerate(testcases):
        result = "%sCase #%s: %s\n" % (result, idx+1, len(re.findall(test, joined_words)))

    return result

if __name__ == "__main__":
    outfile = open("langsolve.out","w")
    
    outfile.write(solve([l.strip() for l in open('atlarge.in','r').readlines()]))
    outfile.close()
