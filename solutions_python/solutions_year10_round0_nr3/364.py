import array
import csv
import os
import sys

def solve(R, k, groups):
    q = array.array('i', groups)
    answer = 0

    history_q = []
    history_boarded = []

    # print q
    r = 0
    while True:
        history_q.append(q[:])

        n_boarded = 0
        q_boarded = array.array('i')

        while q:
            i = q[0]
            if i + n_boarded > k:
                break
            else:
                n_boarded += i
                q.pop(0)
                q_boarded.append(i)

        answer += n_boarded
        q = q + q_boarded
        r += 1
        # print q_boarded, q, answer

        if r == R:
            break

        history_boarded.append(n_boarded)

        if q in history_q:
            idx = history_q.index(q)
            seq_boarded = sum(history_boarded[idx:])
            seq_len = len(history_boarded) - idx

            seq_n_repeat = (R - r) // seq_len
            answer += seq_boarded * seq_n_repeat

            remain_len = (R - r) % seq_len
            remain_boarded = sum(history_boarded[idx:idx + remain_len])
            answer += remain_boarded

            # print seq_n_repeat, seq_len, seq_boarded
            # print 1, remain_len, remain_boarded
            break

    return "%d" % answer

def main(src, dst):
    reader = csv.reader(src, delimiter=" ")

    T = int(reader.next()[0])

    for t in range(T):
        R, k, N = map(int, reader.next())
        groups = map(int, reader.next())
        assert len(groups) == N
        answer = solve(R, k, groups)
        dst.write("Case #%d: %s\n" % (t + 1, answer))

    assert src.read() == ""

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python solve.py input output"
        raise SystemExit

    src_path = os.path.abspath(sys.argv[1])
    src = open(src_path, "r")

    if len(sys.argv) == 2:
        dst = sys.stdout
    else:
        dst_path = os.path.abspath(sys.argv[2])
        if os.path.exists(dst_path):
            raise ValueError("already exists: %s" % dst_path)
        dst = open(dst_path, "w")

    try:
        main(src, dst)
    finally:
        src.close()
        dst.close()
