def main():
    with open('A-large.in', 'r') as f:
        rows = f.readlines()
        N = int(rows[0])
        solutions = []
        for i in xrange(1, N+1):
            row = rows[i]
            splitted = row.split(' ')
            S = splitted[0]
            K = int(splitted[1])
            L = len(S)
            #print("***********************")
            #print("S: " + S)
            counter = 0
            impossible = False
            for j in xrange(0, L-K+1):
                pre_str = S[0:j]
                if "-" in pre_str:
                    impossible = True
                    break
                substr = S[j:j+K]
                post_str = S[j+K:L]
                new_substr = ""
                if substr[0] == "-":
                    for k in xrange(K):
                        if substr[k] == "-":
                            new_substr += "+"
                        else:
                            new_substr += "-"
                    S = pre_str + new_substr + post_str
                    counter += 1
                #print("pre_str: " + pre_str)
                #print("substring " + substr)
                #print("new_substring: " + new_substr)
                #print("post_str: " + post_str)
                #print("new_S: " + S)
            if impossible or "-" in S:
                solutions.append("IMPOSSIBLE")
            else:
                solutions.append(str(counter))

        with open('A-large.out', 'w') as f:
            line_number = 1
            for line in solutions:
                f.write("Case #{0}: {1}\n".format(str(line_number), line))
                line_number += 1     

main()
