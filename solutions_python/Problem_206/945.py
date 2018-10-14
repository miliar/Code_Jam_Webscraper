def speed_ctrl(dist, nb_horses):
    time_lim = 0
    for i in range(nb_horses):
        position, speed = [int(_) for _ in input().split()]
        time_lim = max([(dist - position) / speed, time_lim])
    speed = dist / time_lim
    return speed


def main():
    nb_test = int(input())
    file_out = open('out.txt', 'w')
    for _ in range(nb_test):
        dist, nb_horses = [int(_) for _ in input().split()]
        speed = speed_ctrl(dist, nb_horses)
        print('Case #' + str(_ + 1) + ':', speed, file=file_out)

if __name__ == '__main__':
    main()