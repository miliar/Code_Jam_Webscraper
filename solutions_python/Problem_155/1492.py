t = int(raw_input())


def main():
    for x in range(t):
        line = raw_input().split(" ")
        minimum_shyness, levels = int(line[0]), line[1]
        ovation_count = 0
        friends_needed = 0

        for key, value in enumerate(levels):
            value = int(value)

            '''
            If we hit our else statement, we don't have enough people, for the
            standing ovation, so we need to increase our invited friends
            '''
            if ovation_count + friends_needed >= key:
                ovation_count += value
            else:
                friends_needed = (friends_needed + key) - (ovation_count + friends_needed)
                ovation_count += value

        print "Case #{0}: {1}".format(x + 1, friends_needed)


if __name__ == '__main__':
    main()