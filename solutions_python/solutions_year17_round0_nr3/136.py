import queue


def answer(n, k):
    intervals = queue.PriorityQueue()
    intervals.put_nowait(-n)
    counts = {n: 1}
    k_rem = k

    while not intervals.empty():
        interval = -intervals.get_nowait()
        count = counts[interval]
        left_interval, right_interval = (interval - 1) // 2, interval // 2

        if count >= k_rem:
            return right_interval, left_interval
        k_rem -= count

        del counts[interval]
        for sub_interval in (left_interval, right_interval):
            if sub_interval not in counts:
                intervals.put_nowait(-sub_interval)
                counts[sub_interval] = 0
            counts[sub_interval] += count


def main():
    t = int(input())
    for i in range(1, t + 1):
        n_str, k_str = input().split(" ")
        ma, mi = answer(int(n_str), int(k_str))
        print("Case #{}: {} {}".format(i, ma, mi))


if __name__ == "__main__":
    main()
