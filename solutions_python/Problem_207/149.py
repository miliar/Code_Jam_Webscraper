def solution_simple(n):
    colours = n[1:]
    R,Y,B = colours[0], colours[2], colours[4]
    if R > B+Y or B > R+Y or Y > B+R:
        return 'IMPOSSIBLE'
    result = []
    while R+Y+B:
        #print(result,R,Y,B)
        m = max(R,Y,B)
        if R==m:
            if (result and result[-1] == 'R'):
                if Y>=B:
                    result.append('Y');Y-=1
                else:
                    result.append('B');B-=1                    
            else:
                result.append('R');R -= 1
        elif Y==m:
            if (result and result[-1] == 'Y'):
                if R>=B:
                    result.append('R');R-=1
                else:
                    result.append('B');B-=1
            else:
                result.append('Y');Y-=1
        elif B==m:
            if (result and result[-1] == 'B'):
                if R>=Y:
                    result.append('R');R-=1
                else:
                    result.append('Y');Y-=1
            else:
                result.append('B');B -= 1
    if len(result) > 1 and result[0] == result[-1]:
        result[-2], result[-1] = result[-1], result[-2]
    result = ''.join(result)
    return result

def solution(n):
    R,O,Y,G,B,V = n[1:]
    if R==G and 0== O+Y+B+V:
        return 'RG' * G
    elif Y==V and 0== R+O+G+B:
        return 'YV' * V
    elif B==O and 0== R+Y+G+V:
        return 'BO'* B

    R -= G
    Y -= V
    B -= O
    simple = solution_simple([0,R,O,Y,G,B,V])
    if simple == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'
    if G:
        if 'R' not in simple:
            return 'IMPOSSIBLE'
        i = simple.index('R')
        simple = simple[:i] + 'RG' * G + simple[i:]
    if V:
        if 'Y' not in simple:
            return 'IMPOSSIBLE'
        i = simple.index('Y')
        simple = simple[:i] + 'YV' * V + simple[i:]
    if O:
        if 'B' not in simple:
            return 'IMPOSSIBLE'
        i = simple.index('B')
        simple = simple[:i] + 'BO' * O + simple[i:]
    return simple

if __name__ == "__main__":
    FILE_NAME = 'B-large'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()

            case = 1
            i = 1
            while i < len(r):
                #buf = []
                #n, k = map(int, r[i].split())
                #for j in range(n):
                #    buf.append(r[j])
                answer = 'Case #%d: %s\n' % (case, solution(map(int, r[i].split())))
                w.write(answer)
                print(answer)
                case += 1
                i += 1