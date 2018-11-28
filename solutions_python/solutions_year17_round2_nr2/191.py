import sys

def dprint(*things):
    #return  # Disable `dprint` function
    for thing in things:
        print >> sys.stderr, thing,
    print >> sys.stderr, ""


def read_input():
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    horses = {}
    horses["r"] = R
    horses["o"] = O
    horses["y"] = Y
    horses["g"] = G
    horses["b"] = B
    horses["v"] = V
    return N, horses

#def valid_neighbors_small(color):
#    if color == None

def valid_neighbors(color):
    if color == None:
        return "roygbv"

    elif color == "r":
        return "ygb"

    elif color == "o":  # r + y
        return "b"  # b

    elif color == "y":
        return "rbv"

    elif color == "g":  # y + b
        return "r"

    elif color == "b":
        return "roy"

    elif color == "v":  # r + b
        return "y"

    else:
        dprint("ERROR!")

def invalid_neighbors(color):
    if color == None:
        return ""

    elif color == "r":
        return "rov"

    elif color == "o":  # r + y
        return "orygv"  # b

    elif color == "y":
        return "yog"

    elif color == "g":  # y + b
        return "gybov"  # r

    elif color == "b":
        return "bgv"

    elif color == "v":  # r + b
        return  "vrbog"  # y

    else:
        dprint("ERROR!")

def my_cp(dct):
    new_dct = {}
    for k in dct.keys():
        if not dct[k]:
            continue
        new_dct[k] = dct[k]
    return new_dct

def dfs(horses, ans_str, N):
    if len(ans_str) == N:
        if ans_str[0] in invalid_neighbors(ans_str[-1]):
            return None
        return ans_str
    last_horse = None if not ans_str else ans_str[-1]
    #dprint(ans_str)
    for clr in horses.keys():
        if horses[clr] == 0:
            continue
        if clr in invalid_neighbors(last_horse):
            continue
        horses[clr] -= 1
        result = dfs(horses, ans_str + clr, N)
        if result:
            return result
        horses[clr] += 1
    return None

import operator
def get_xyz(horses, long_str, N):
    x, y, z = sorted(horses.items(), key=operator.itemgetter(1), reverse=True)
    if x[1] == y[1]:
        ans = (x[0] + y[0] + z[0]) * z[1] + \
                (x[0] + y[0]) * (y[1] - z[1])
    elif x[1] <= y[1] + z[1]:
        y_part = x[1] - z[1]
        z_part = x[1] - y[1]
        yz_part = x[1] - y_part - z_part
        ans = (x[0] + y[0]) * y_part + \
                (x[0] + y[0] + z[0]) * yz_part + \
                (x[0] + z[0]) * z_part
    else:
        ans = None
        return ans

    #dprint(long_str)
    for key, ss in long_str.items():
        ans = ans.replace(key, ss, 1)
    if len(ans) != N:
        dprint(ans[:10], ans[-10:])
        dprint(len(ans), N, x, y, z)
        dprint(y_part, yz_part, z_part)
    return ans


def gen(x, y, n):
    return (x + y) * n + x

def calculate(input_args):
    N, horses = input_args
    #dprint(horses)

    hb, hr, hy = horses["b"], horses["r"], horses["y"]
    if horses["b"] == horses["o"] and hb != 0:
        if hr == 0 and hy == 0:
            return "bo" * hb
        else:
            return None
    elif horses["r"] == horses["g"] and hr != 0:
        if hb == 0 and hy == 0:
            return "rg" * hr
        else:
            return None
    elif horses["y"] == horses["v"] and hy != 0:
        if hb == 0 and hr == 0:
            return "yv" * hy
        else:
            return None
    elif horses["b"] < horses["o"]:
        return None
    elif horses["r"] < horses["g"]:
        return None
    elif horses["y"] < horses["v"]:
        return None

    horses["b"] -= horses["o"]
    horses["r"] -= horses["g"]
    horses["y"] -= horses["v"]
    if horses["b"] < 0 or horses["r"] < 0 or horses["y"] < 0:
        dprint("ERR")
        return None

    b_ans = gen("b", "o", horses["o"])
    r_ans = gen("r", "g", horses["g"])
    y_ans = gen("y", "v", horses["v"])
    del horses["o"]
    del horses["g"]
    del horses["v"]

    ans = {"b": b_ans, "r": r_ans, "y": y_ans}
    """
    if_zero = (horses["b"] == 0, horses["r"] == 0, horses["y"] == 0)
    cnt = if_zero.count(True)
    if cnt == 3:
        dprint("ERR")
        return None
    elif cnt == 3:
        dprint("ERR")
        return None
        # True
    """

    return get_xyz(horses, ans, N)

def to_formated_string(result_tokens):
    if result_tokens:
        ans_str = result_tokens.upper()
        if ans_str[0] == ans_str[-1]:
            dprint(ans_str[0], ans_str[-1])
    else:
        ans_str = "IMPOSSIBLE"
    return ans_str

if __name__ == '__main__':
    T = int(raw_input())
    case = 1
    while case <= T:
        input_args = read_input()
        result = calculate(input_args)
        answer = to_formated_string(result)
        print 'Case #%d:' % case, answer
        case += 1

