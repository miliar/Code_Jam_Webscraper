import sys
sys.setrecursionlimit(100000)

COOKIES_PER_SECOND = 2


def get_cookie_results(
    cookie_rate,
    farm_price,
    farm_rate,
    goal_cookies
):

    farm_buy_seconds = farm_price / cookie_rate
    to_win_seconds = goal_cookies / cookie_rate
    if to_win_seconds < farm_buy_seconds or to_win_seconds < farm_buy_seconds+ goal_cookies / (cookie_rate + farm_rate):
        return to_win_seconds
    else:
        return min(
            to_win_seconds,
            farm_buy_seconds + get_cookie_results(
                cookie_rate + farm_rate,
                farm_price,
                farm_rate,
                goal_cookies
            )
        )


def main(argv=sys.argv):

    count = int(sys.stdin.readline())
    for i in range(count):
        farm_price, farm_rate, goal_cookies = map(
            float, sys.stdin.readline().split(' ')
        )

        sys.stdout.write(
            'Case #{0}: {1}\n'.format(
                i+1,
                get_cookie_results(
                    COOKIES_PER_SECOND,
                    farm_price,
                    farm_rate,
                    goal_cookies
                )
            )
        )
if __name__ == '__main__':
    main()
