map = {' ':' ', 'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

num_lines = int(raw_input())

for i in range(num_lines):
    in_str = raw_input()
    out_str = ""
    for c in in_str:
        out_str += map[c]
    print "Case #{0}: ".format(i+1) + out_str 