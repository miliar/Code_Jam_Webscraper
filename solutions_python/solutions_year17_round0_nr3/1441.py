from collections import deque
import heapq
# [G] [ ] [ ] [P] [ ] [ ] [G]


def solution_dequeue(stalls, people):
    distances = deque((stalls,))
    left, right = stalls, stalls
    while people:
        people -= 1
        dist = distances.popleft()
        left = dist // 2
        right = dist - left
        left, right = (left, right) if left >= right else (right, left)
        left -= 1
        left, right = (left, right) if left >= right else (right, left)
        distances.append(left)
        distances.append(right)
    return '{} {}'.format(left, right)


def solution_heap(stalls, people):
    distances = [-stalls]
    left, right = stalls, stalls
    while people:
        people -= 1
        dist = - heapq.heappop(distances)
        left = dist // 2
        right = dist - left
        left, right = (left, right) if left >= right else (right, left)
        left -= 1
        left, right = (left, right) if left >= right else (right, left)
        heapq.heappush(distances, -left)
        heapq.heappush(distances, -right)
    return '{} {}'.format(left, right)


def solution(stalls, people):
    distances = [stalls]
    left, right = stalls, stalls
    while people:
        people -= 1
        index, dist = max(enumerate(distances), key=lambda item: item[-1])
        left = dist // 2
        right = dist - left - 1
        distances[index] = left
        distances.append(right)
    return '{} {}'.format(max(left, right), min(left, right))


def process(filepath):
    with open(filepath.replace('.in', '.out'), 'w') as outp:
        with open(filepath) as filep:
            inputs = None
            case = 0
            for line in filep:
                line = line.strip()
                if inputs is None:
                    inputs = int(line)
                else:
                    case += 1
                    stalls, people = line.split(' ', 1)
                    result = 'Case #{}: {}\n'.format(case, solution_heap(int(stalls), int(people)))
                    print(result, end='')
                    outp.write(result)


if __name__ == '__main__':
    process('C-small-2-attempt1.in')