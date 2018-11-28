import sys

def dprint(*things):
    #return  # Disable `dprint` function
    for thing in things:
        print >> sys.stderr, thing,
    print >> sys.stderr, ""


def read_input():
    all_km, N_horses = map(int, raw_input().split())
    horses = []
    for _ in range(N_horses):
        start_km, speed = map(int, raw_input().split())
        horses.append((start_km, speed))
    return all_km, horses

def calculate(input_args):
    all_km, horses = input_args
    hr_list = []
    for st, speed in horses:
        hr = (all_km - st) / (speed + 0.0)
        hr_list.append(hr)
    max_hr = max(hr_list)
    if max_hr == 0:
        dprint(all_km, horses)
    ans = all_km / (max_hr + 0.0)
    return ans

def to_formated_string(result_tokens):
    ans = result_tokens
    ans_str = "%.6f" % ans
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

