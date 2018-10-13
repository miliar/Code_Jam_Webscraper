__author__ = 'Adela'


import collections

def main():
    t = int(input())

    for i in range(t):

        n = int(input())
        naomi = [float(k) for k in input().split()]
        ken = [float(k) for k in input().split()]
        naomi.sort()
        ken.sort()

        score_x = 0
        deq = collections.deque(ken)
        # Deceitful War
        for elem in naomi:
            if elem < deq[0]:
                # if the smallest block of naomi is smaller than the smallest block of ken
                # lose it, but lie
                deq.pop()
            else:
                # naomi will win the point because she will lie again
                deq.popleft()
                score_x += 1

        score_y = 0
        deq = collections.deque(ken)
        # War
        for elem in naomi:
            won = False
            len_deq = len(deq)
            for j in range(len_deq):
                if not won and deq[j] > elem:
                    deq.remove(deq[j])
                    won = True
            if not won:
                deq.popleft()
                score_y += 1

        print("Case #", i + 1, ": ", score_x, " ", score_y, sep='')


if __name__ == "__main__":
    main()
