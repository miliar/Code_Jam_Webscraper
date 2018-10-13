#!/usr/bin/env python

from collections import deque

FILENAME = 'D-large.in'

def load_dataset(q):
    result = deque()

    block_count = q.popleft()

    result.append(int(block_count))
    result.append([float(n) for n in q.popleft().split()])
    result.append([float(n) for n in q.popleft().split()])

    return result

def load_from_file():
    result = None

    with open(FILENAME) as f:
        result = [line.rstrip('\n') for line in f]

    return deque(result)

def crap(plays, n, k):
    print "plays:  " + str(plays)

    bottom_n = deque(n)
    bottom_k = deque(k)
    bottom_points = 0
    for x in reversed(xrange(plays)):
        weight_n = bottom_n.popleft()
        weight_k = bottom_k.popleft()

        rotations = 0
        while weight_n > weight_k:
            bottom_k.append(weight_k)
            rotations += 1

            if rotations > x:
                rotations = 0
                break
            weight_k = bottom_k.popleft()

        bottom_k.rotate(rotations)

        if weight_n > weight_k:
            bottom_points += 1


# assumes hand is sorted 0<1
def ken_play(hand, challenge):
    hand_size = len(hand)

    # optimize for everything is a loss
    if challenge > hand[hand_size - 1]:
        weight = hand.popleft()
        return weight

    weight = hand.popleft()

    tries = 0
    while challenge > weight:
        hand.append(weight)
        tries += 1

        weight = hand.popleft()
        if tries >= hand_size:
            tries = 0
            break

    hand.rotate(tries)

    return weight

def ken_optimize(hand, challenge):
    hand_size = len(hand)
    increment = 0.0000001

    if challenge > hand[hand_size - 1]:
        # everything in hand is a loss
        weight = hand.popleft()
        return weight
    elif hand[hand_size - 1] == (challenge + 0.0000001):
        #forcing biggest card
        weight = hand.pop()
        return weight

    # crappy normal play
    weight = hand.popleft()

    tries = 0
    while challenge > weight:
        hand.append(weight)
        tries += 1

        weight = hand.popleft()
        if tries >= hand_size:
            tries = 0
            break

    hand.rotate(tries)

    return weight


def play_normal(plays, n, k):
    naomi = deque(n)
    ken = deque(k)
    points = 0

    for x in reversed(xrange(plays)):
        weight_n = naomi.pop()
        weight_k = ken_play(ken, weight_n)

        if weight_n > weight_k:
            points += 1

    return points

def play_dirty(plays, n, k):
    naomi = deque(n)
    ken = deque(k)
    points = 0

    for x in reversed(xrange(plays)):
        weight_n = naomi.popleft()
        k_lowest = ken[0]
        k_highest = ken[x]

        weight_k = -1
        if k_lowest > weight_n:
            # this is our smallest weight; it can never win
            # make ken burn his highest
            #weight_k  = ken_play(ken, k_highest - 0.0000001)
            weight_k  = ken_optimize(ken, k_highest - 0.0000001)
        else:
            # make ken throw away his lowest for losing
            #weight_k = ken_play(ken, k_highest + 0.0000001)
            weight_k = ken_optimize(ken, k_highest + 0.0000001)

        if weight_n > weight_k:
            points += 1

    return points


def dirty_save(plays, n, k):
    naomi = deque(n)
    ken = deque(k)
    points = 0

    for x in reversed(xrange(plays)):
        weight_n = naomi.popleft()
        k_highest = ken[x]

        weight_k = -1
        if k_highest > weight_n:
            # make ken throw away his highest
            weight_k = ken_play(ken, k_highest - 0.0000001)
        else:
            weight_k = ken_play(ken, weight_n)

        if weight_n > weight_k:
            points += 1

    return points




def main():
    data = load_from_file()
    number_of_cases = int(data.popleft())

    for x in range(0, number_of_cases):
        case = load_dataset(data)

        blocks = case.popleft()
        naomi = sorted(case.popleft())
        ken = sorted(case.popleft())

        normal_points = play_normal(blocks, naomi, ken)
        dirty_points = play_dirty(blocks, naomi, ken)

        print "Case #" + str(x+1) + ": " + str(dirty_points) + " " + str(normal_points)


if __name__ == "__main__":
    main()
