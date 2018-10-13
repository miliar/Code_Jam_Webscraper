def bad_colors(color):
    if color == 'R':
        return ['R', 'O', 'V']
    if color == 'B':
        return ['B', 'G', 'V']
    if color == 'Y':
        return ['Y', 'O', 'G']
    if color == 'O':
        return ['O', 'R', 'Y']
    if color == 'V':
        return ['R', 'O', 'B']
    if color == 'G':
        return ['G', 'B', 'Y']
    
def max_color(colors, colors_used):
    most = 0
    best = ""
    for color in colors:
        if colors[color] > most or most == 0:
            best = color
            most = colors[color]
        elif colors[color] == most and colors_used[color] > colors_used[best]:
            best = color
    return best

fileIn = open('B-small-attempt2.in','r')
fileOut = open('out.txt','w',1)

T = int(fileIn.readline().strip())
for t in range(1, T+1):
    N, R, O, Y, G, B, V = [int(x) for x in fileIn.readline().strip().split()]
    colors = {'R':R, 'O':O, 'Y':Y, 'G':G, 'B':B, 'V':V}
    colors_used = {'R':0, 'O':0, 'Y':0, 'G':0, 'B':0, 'V':0}
    RedMane = R+V+O
    BlueMane = B+G+V
    YellowMane = Y+O+G
    fileOut.write("Case #"+str(t)+": ")
    if (RedMane > int(N/2)) or  (BlueMane > int(N/2)) or (YellowMane > int(N/2)):
        fileOut.write('IMPOSSIBLE\n')
    else:
        color_str = max_color(colors, colors_used)
        colors[color_str] = colors[color_str] - 1
        colors_used[color_str] = colors_used[color_str] + 1
        N = N - 1
        while N > 0:
            good_colors = {c:colors[c] for c in colors if (not c in bad_colors(color_str[-1:]))}
            best_color = max_color(good_colors, colors_used)
            color_str = color_str + best_color
            colors[best_color] = colors[best_color] - 1
            colors_used[best_color] = colors_used[best_color] + 1
            N = N - 1
        fileOut.write(color_str+'\n')



fileOut.close()
fileIn.close()
