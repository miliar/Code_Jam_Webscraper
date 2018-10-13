# Problem C. Bathroom Stalls


queue = []
last_split1 = None
last_split2 = None


def occupy_stall():
    global queue
    global last_split1
    global last_split2
    top_interval = queue[0]
    del queue[0]
    stall_no = (top_interval[1] + top_interval[0]) / 2
    interval1 = (top_interval[0], stall_no, stall_no - top_interval[0])
    interval2 = (stall_no, top_interval[1], top_interval[1] - stall_no)
    queue.append(interval1)
    queue.append(interval2)
    last_split1 = interval1
    last_split2 = interval2
    queue = sorted(queue, key=lambda x: (-x[2], x[0]))
    return None


def main():
    t = int(raw_input())

    for i in range(1, t+1):
        global queue
        global last_split1
        global last_split2
        queue = []
        last_split1 = None
        last_split2 = None
        #n, m =[1000,1000]
        n, m = [int(s) for s in raw_input().split(" ")]

        interval = [0, n + 1, n + 1]
        queue.append(interval)
        occupy_stall()

        while m > 1:

            occupy_stall()

            m -= 1

        mini = min(last_split1[2], last_split2[2]) - 1
        maxi = max(last_split1[2], last_split2[2]) - 1


        print("Case #{}: {} {}".format(i, maxi, mini))

    return None

main()
