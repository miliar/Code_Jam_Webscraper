#!/usr/bin/python


def main():
    T = int(raw_input())
    for t in xrange(T):
        tokens = raw_input().split()
        C = float(tokens[0])
        F = float(tokens[1])
        X = float(tokens[2])

        best_time = X / 2
        curr_time = 0
        curr_speed = 2

        while True:
            if curr_time > best_time:
                break

            best_time = min(best_time, curr_time + X / curr_speed)
            curr_time += C / curr_speed
            curr_speed += F

        print "Case #{}: {:.7f}".format(t+1, best_time)

if __name__ == '__main__':
    main()
