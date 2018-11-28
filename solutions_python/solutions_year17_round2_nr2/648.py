def update_colors(t, n):
    """
    
    :param t: all colors 
    :param n: next color
    :return: 
    """
    if n == "R":
        t[0] -= 1
    if n == "B":
        t[1] -= 1
    if n == "Y":
        t[2] -= 1
    return t

def choose_color(c, i, t):
    """
    
    :param c: current color 
    :param i: initial color
    :param t: all colors
    :return: next color
    """
    if c == "R":
        if t[2] == t[1] and i != c:
            return i
        else:
            return 'Y' if t[2] > t[1] else 'B'
    if c == "B":
        if t[2] == t[0] and i != c:
            return i
        else:
            return 'Y' if t[2] > t[0] else 'R'
    if c == "Y":
        if t[1] == t[0] and i != c:
            return i
        else:
            return 'B' if t[1] > t[0] else 'R'


def create_string(R, O, Y, G, B, V):
    res = ''
    for r in range(R):
        res += 'R'
    for r in range(O):
        res += 'O'
    for r in range(Y):
        res += 'Y'
    for r in range(G):
        res += 'G'
    for r in range(B):
        res += 'B'
    for r in range(V):
        res += 'V'
    return res

def share_color(x, y):
    reds = ['R', 'O', 'V']
    blues = ['B', 'V', 'G']
    yellows = ['Y', 'G', 'O']
    if x=='R':
        if y in reds:
            return True
        return False
    if x=='B':
        if y in blues:
            return True
        return False
    if x=='Y':
        if y in yellows:
            return True
        return False
    if x=='O':
        if y in reds or y in yellows:
            return True
        return False
    if x=='V':
        if y in reds or y in blues:
            return True
        return False
    if x=='G':
        if y in blues or y in yellows:
            return True
        return False
    return False

def opposite_color(x, y):
    if x=='R':
        if y=='G':
            return True
        return False
    if x=='B':
        if y=='O':
            return True
        return False
    if x=='Y':
        if y=='V':
            return True
        return False
    if x=='O':
        if y=='B':
            return True
        return False
    if x=='V':
        if y=='Y':
            return True
        return False
    if x=='G':
        if y=='R':
            return True
        return False
    return False



def check_res(S):
    x = [share_color(S[i+1], S[i]) for i in range(len(S)-1)]
    x.append(share_color(S[0], S[len(S)-1]))
    return all(a == False for a in x)

def determine_placement(N, R, O, Y, G, B, V):
    """
    
    :param N: 
    :param R: 
    :param O: 
    :param Y: 
    :param G: 
    :param B: 
    :param V: 
    :return: 
    """
    # contain red   : R+O+V
    # contain blue  : B+V+G
    # contain yellow: Y+O+G
    if any(x > N//2 for x in [R+O+V, B+V+G, Y+O+G]):
        return None
    if R < G or B < O or Y < V:
        return None

    res = ''
    for i in range(G):
        res += 'RG'
        G -= 1
        R -= 1
        if G==0 and R>0:
            res += 'R'
    for i in range(O):
        res += 'BO'
        B -= 1
        O -= 1
        if O==0 and B>0:
            res += 'B'
    for i in range(V):
        res += 'YV'
        Y -= 1
        V -= 1
        if V==0 and Y>0:
            res += 'Y'
    res = list(res)

    # At this point I am left with only R, B, Y
    colors = [R, B, Y]
    if len(res) == 0:
        c = colors.index(max(colors))
        if c==0:
            res.append('R')
        if c==1:
            res.append('B')
        if c==2:
            res.append('Y')
        colors[c] -= 1
    initialColor = res[0]
    while any(x>0 for x in colors):
        currentColor = res[-1]
        nextColor = choose_color(currentColor, initialColor, colors)
        colors = update_colors(colors, nextColor)
        res.append(nextColor)





    # res = create_string(R, O, Y, G, B, V)
    # res = list(res)
    # for i in range(1,N):
    #     if share_color(res[i], res[i-1]):
    #         try:
    #             idx = [opposite_color(x, res[i-1]) for x in res[i:]].index(True)
    #         except ValueError:
    #             try:
    #                 idx = [share_color(x, res[i - 1]) for x in res[i:]].index(False)
    #             except ValueError:
    #                 return None
    #         idx += i
    #         res[i], res[idx] = res[idx], res[i]
    # for i in range(1,N):
    #     if share_color(res[-i], res[-i+1]):
    #         try:
    #             idx = [opposite_color(x, res[-i+1]) for x in res[:-i][::-1]].index(True)
    #         except ValueError:
    #             try:
    #                 idx = [share_color(x, res[i - 1]) for x in res[i:]].index(False)
    #             except ValueError:
    #                 return None
    #         idx = N-idx-i
    #         res[-i], res[idx] = res[idx], res[-i]

    if check_res(res):
        return ''.join(res)
    return None


with open("./B-small-attempt0.in", "r") as fin:
    with open("./B-small-attempt0.out", "w+") as fout:
        T = int(fin.readline().strip("\n"))

        for i in range(T):
            N, R, O, Y, G, B, V = fin.readline().strip("\n").split()
            N, R, O, Y, G, B, V = int(N), int(R), int(O), int(Y), int(G), int(B), int(V)
            res = determine_placement(N, R, O, Y, G, B, V)
            if isinstance(res, str):
                fout.write("Case #%d: %s\n" % (i + 1, res))
            else:
                fout.write("Case #%d: IMPOSSIBLE\n" % (i + 1))
