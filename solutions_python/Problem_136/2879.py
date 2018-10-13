import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())

    for _t in range(t):
        arr = [float(x) for x in f.readline().split()]
        current_rate = 2.0
        previous_time = arr[2]/current_rate
        y = 0
        while True:
            y = y + arr[0]/current_rate
            current_rate = current_rate + arr[1]
            current_time = y + arr[2]/current_rate
            if current_time < previous_time:
                previous_time = current_time
            else:
                break
        print ("Case #%d: %f"%(_t+1, previous_time))
