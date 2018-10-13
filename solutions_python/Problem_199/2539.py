def sol_print(value):
    sol_print.line_number += 1
    print "Case #%d: %s"%(sol_print.line_number, value)


def flip_in_place(cookies, index, size):
    for idx, cookie in enumerate(cookies):
        if idx in range(index, index + size):
            if cookie == '-':
                cookies[idx] = '+'
            else:
                cookies[idx] = '-'


def solve_cookies_line(cookies, size):
    cookies_max_idx = len(cookies) - 1
    sol = 0
    for idx, cookie in enumerate(cookies):
        if cookie == '-':
            if idx + size - 1 <= cookies_max_idx:
                flip_in_place(cookies, idx, size)
                sol += 1
            else:
                return "IMPOSSIBLE"
    if '-' in cookies:
        return "IMPOSSIBLE"
    return sol


def main():
    sol_print.line_number = 0
    lines = int(raw_input())
    for number in range(lines):
        input = str(raw_input())
        cookies, size = input.split()
        sol_print(solve_cookies_line(list(cookies), int(size)))

if __name__ == "__main__":
    main()
