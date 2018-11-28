
def main():
    file = open('C-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))

    for case_idx in range(0, case_count):

        stalls_users = next(lines).split()
        stalls = int(stalls_users[0])
        users = int(stalls_users[1])

        last_stalls = -1
        user_ordinal = 1

        while last_stalls == -1:
            ordinal = user_ordinal * 2

            if ordinal > users:
                stalls_available = stalls - (user_ordinal - 1)
                first_set_size = stalls_available // user_ordinal
                reminder = stalls_available % user_ordinal

                last_user_idx = users - user_ordinal
                last_stalls = first_set_size

                if last_user_idx < reminder:
                    last_stalls += 1
            else:
                user_ordinal = ordinal

        available_stalls = last_stalls // 2
        s_max = available_stalls
        if last_stalls % 2 == 0:
            available_stalls -= 1
        s_min = available_stalls

        print(f'Case #{case_idx  + 1}: {s_max} {s_min}')


if __name__ == '__main__':
    main()
