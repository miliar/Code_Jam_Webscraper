def solution(answer1, array1, answer2, array2):
    row1 = set(array1[answer1-1])
    row2 = set(array2[answer2-1])
    inter = set.intersection(row1, row2)
    if len(inter) == 0:
        return "Volunteer cheated!"
    elif len(inter) > 1:
        return "Bad magician!"
    else:
        return inter.pop()


    


if __name__ == '__main__':
    with open('test.txt') as in_stream:
        with open('result.txt', 'w') as out_stream:
            t = int(in_stream.readline())
            for c in xrange(t):
                answer1 = int(in_stream.readline())
                array1 = [map(int, in_stream.readline().strip().split(' ')) for _ in xrange(4)]
                answer2 = int(in_stream.readline())
                array2 = [map(int, in_stream.readline().strip().split(' ')) for _ in xrange(4)]
                result = solution(answer1, array1, answer2, array2)
                out_stream.write("Case #{}: {}\n".format(c+1, result))





