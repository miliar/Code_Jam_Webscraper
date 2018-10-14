from sys import stdin

def compress_string(string):
    result = string[0]
    for char in string[1:]:
        if result[-1] != char:
            result += char
    return result

def handle_case(f):
    num_strings = int(f.readline().strip())

    strings = []
    for i in range(num_strings):
        strings.append(f.readline().strip())

    base_string = compress_string(strings[0])
    impossible = False
    for string in strings[1:]:
        if base_string != compress_string(string):
            impossible = True
            break

    if impossible:
        # Seriously what kind of name is Fegla? I got it wrong the first time
        # for typing Felga...though that's kind of weird too... :p
        print "Fegla Won"
        return

    vectors = convert_to_vectors(strings)
    min_dist = compute_min_dist(vectors)
    print min_dist
    return

def convert_to_vector(string):
    vector = [1]
    for i, char in enumerate(string[1:]):
        if char == string[i]:
            vector[-1] += 1
        else:
            vector.append(1)
    return vector

def convert_to_vectors(strings):
    vectors = [convert_to_vector(string) for string in strings]
    return vectors


def mean(points):
    n = len(points)
    sum = 0
    for point in points:
        sum += point
    return int(round(float(sum)/n))


def compute_min_dist(vectors):
    dist = 0
    n = len(vectors[0])
    for i in range(n):
        points = [vector[i] for vector in vectors]
        mid_point = mean(points)
        for point in points:
            dist += abs(point - mid_point)
    return dist


if __name__ == '__main__':
    num_cases = int(stdin.readline().strip())

    for i in range(num_cases):
        print "Case #%s:" % (i + 1),
        handle_case(stdin)
