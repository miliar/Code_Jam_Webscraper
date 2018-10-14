"""
Cookie Clicker
"""

C = 500.
F = 4.
X = 2000.
BASE = 2.

from itertools import count, izip

def iter_time_to_farm(C, F, X, B):
    yield 0
    for n in count():
        yield C / (B + (n * F))
        
def iter_time_for_farms(C, F, X, B):
    total = 0
    for time_for_farm in iter_time_to_farm(C, F, X, B):
        total += time_for_farm
        yield total
        
def iter_time_to_finish(C, F, X, B):
    for n in count():
        yield X / (B + (n * F))

def iter_time_to_win(C, F, X, B):
    for farms, finish in izip(iter_time_for_farms(C, F, X, B),
                              iter_time_to_finish(C, F, X, B)):
        yield farms + finish

def calc(C, F, X, B):
    times = iter_time_to_win(C, F, X, B)
    minimum = times.next()
    for time in times:
        if time > minimum:
            return minimum
        minimum = time

def cookify(cookies, farms, total_time):
    if cookies >= X:
        return total_time
    if total_time >= X / BASE:
        return total_time
    cookies_per_second = BASE + (F * farms)
    time_to_next_farm = (C - cookies) / cookies_per_second
    time_to_finish = (X - cookies) / cookies_per_second
    
    return min(total_time + time_to_finish, cookify(0, farms + 1, total_time+time_to_next_farm))
    
    # if time_to_finish <= time_to_next_farm:
        # return time_to_finish
    
    # return cookify(0, farms + 1, total=cookies - C) + time_to_next_farm
    
    
def parse_input(lines):
    lines = iter(lines)
    number_of_cases = int(lines.next())
    results = []
    for case in range(number_of_cases):
        C, F, X = [float(x) for x in lines.next().split(" ")]
        # results.append(cookify(0, 0, 0))
        # results.append(calc(C, F, X, BASE))
        yield calc(C, F, X, BASE)
    
    # return results
    
sample = """4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0"""
    
def main():
    import sys
    input_file = sys.argv[1]
    lines = open(input_file, "rb").readlines()
    results = parse_input(lines)
    output = []
    with open("cookies2.out", "wb") as f:
        for i, r in enumerate(results, 1):
            f.write("Case #%d: %.7f\n" % (i, r,))
    
    
        # f.write("\n".join(output))
    
if __name__ == '__main__':
    main()