def recycles(bigger_brother):
    returned = set()
    smaller_brother = str(bigger_brother)
    for i in range(len(smaller_brother)):
        smaller_brother = str(smaller_brother)[1:] + str(smaller_brother)[:1]
        if int(smaller_brother) < bigger_brother and smaller_brother[0] != '0':
            if smaller_brother not in returned:
                returned.add(smaller_brother)
                yield int(smaller_brother)


def recycled_nums_between(A, B):
    for bigger_brother in range(A, B + 1):
        for smaller_brother in recycles(bigger_brother):
            if A <= smaller_brother <= B:
                yield smaller_brother 

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        print('Case #{num}: {answer}'.format(
                num=i+1,
                answer=len(list(recycled_nums_between(*map(int, raw_input().split()))))
                ))
