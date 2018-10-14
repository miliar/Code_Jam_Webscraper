#! /usr/bin/python

def solve(n, queue, comb, op):
    answer = [queue[0]]
    for i in range(1,n):
        cur = queue[i]
        l = len(answer)
        if l>0:
            if (answer[l-1]+cur) in comb:
                answer[l-1]=comb[answer[l-1]+cur]
            elif cur in op:
                if op[cur] in answer:
                    answer = []
                else:
                    answer.append(cur)
            else:
                answer.append(cur)
        else:
            answer.append(cur)
    out = '['
    l = len(answer)
    if l>0:
        for i in range(0,l-1):
            out = out + ('%s, '%answer[i])
        out = out + ('%s'%answer[l-1])
    out = out + ']'
    return out

if __name__ == "__main__":
    f = open("data.in","r")
    g = open("data.out","w")
    cases = int(f.readline().split()[0])
    for case in range(1,cases+1):
        line = f.readline().split()
        idx_line = 0
        c = int(line[idx_line])
        comb = dict()
        for i in range(1,c+1):
            idx_line = idx_line+1
            str = line[idx_line]
            comb[str[0]+str[1]] = str[2]
            comb[str[1]+str[0]] = str[2]
        idx_line = idx_line+1
        d = int(line[idx_line])
        opp = dict()
        for i in range(1,d+1):
            idx_line = idx_line+1
            str = line[idx_line]
            opp[str[0]] = str[1]
            opp[str[1]] = str[0]
        idx_line = idx_line+1
        n = int(line[idx_line])
        idx_line = idx_line+1
        queue = line[idx_line]
        answer = solve(n, queue, comb, opp)
        g.write("Case #%d: %s\n" % (case,answer))
    f.close()
    g.close()