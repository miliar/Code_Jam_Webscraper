import sys

def pal_squares_fast(X):
    cur_left = 1
    ans = 0
    while True:
        combined = str(cur_left) + str(cur_left)[::-1]
        int_combined = int(combined)
        squared = int_combined**2
        if squared < X and str(squared) == str(squared)[::-1]:
            ans += 1

        if cur_left > 9:
            combined = str(cur_left) + str(cur_left)[:-1][::-1]
            int_combined = int(combined)
            squared = int_combined**2
            if squared >= X: break
            if str(squared) == str(squared)[::-1]:
                ans += 1

        cur_left += 1
    return ans+3

def pal_squares_below(X):
    if X > 10:
        return pal_squares_fast(X)
    squares_list = []
    cr = 1
    while cr*cr < X:
        if int(str(cr)[0]) <= 3 and str(cr) == str(cr)[::-1]:
            squares_list.append(cr*cr)
        cr += 1
    return_value = 0
    for elem in squares_list:
        if str(elem) == str(elem)[::-1]:
            return_value += 1
    return return_value

def solve():
    A,B = map(int,sys.stdin.readline().strip().split())
    print pal_squares_below(B+1)-pal_squares_below(A)

def run():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        sys.stdout.write("Case #"+str(i+1)+": ")
        solve()

if __name__ == "__main__":
    run()
