#import re
import string

if __name__ == "__main__":
#    regex = re.compile("\.+")
    fin = open('A-large.in', 'r')
    fout = open('A-large.out', 'w')
    # T test cases
    T = int(fin.readline())
    for i in xrange(T):
        N, K = [int(x) for x in fin.readline().split()]

        lines = [0] * N
        for j in xrange(N):
            lines[j] = fin.readline().strip()
            line = string.replace(lines[j], '.', '')
#            line = regex.sub('', lines[j])
            lines[j] = "."*(N-len(line)) + line

        found = {}
        found["R"] = False
        found["B"] = False
        for j in xrange(N):
            first_index = -1
            if found["R"]:
                if found["B"]: break
                else:
                    first_b = lines[j].find("B")
                    if first_b >= 0: first_index = first_b
                    else: continue #red done, no blues in row
            elif found["B"]:
                first_r = lines[j].find("R")
                if first_r >= 0: first_index = first_r
                else: continue #blue done, no reds in row
            else:
                first_r = lines[j].find("R")
                first_b = lines[j].find("B")
                first_index = -1
                if first_r == -1:
                    if first_b == -1: continue #no blues or reds in row
                    else: first_index = first_b
                elif first_b == -1:
                    first_index = first_r
                else:
                    first_index = first_r if first_r < first_b else first_b
            for index in xrange(first_index, N):
                color = lines[j][index]
                if found[color]: continue

                found[color] = True
                for k in xrange(1, K):
                    if index-k < 0 or j+k >= N or lines[j+k][index-k] != color:
                        found[color] = False
                        break
                if found[color]: continue

                found[color] = True
                for k in xrange(1, K):
                    if j+k >= N or lines[j+k][index] != color:
                        found[color] = False
                        break
                if found[color]: continue
                
                found[color] = True
                for k in xrange(1, K):
                    if index+k >=N or j+k >= N or lines[j+k][index+k] != color:
                        found[color] = False
                        break
                if found[color]: continue

                found[color] = True
                for k in xrange(1, K):
                    if index+k >= N or lines[j][index+k] != color:
                        found[color] = False
                        break
                if found[color]: continue
        result = ""
        if found["R"]:
            if found["B"]: result = "Both"
            else: result = "Red"
        elif found["B"]: result = "Blue"
        else: result = "Neither"
        fout.write("Case #" + str(i+1) + ": " + result + "\n")
    fin.close()
    fout.close()
            
