def first_attempt():
    output_str = 'Case #{}: {}'
    num_cases = int(input())
    for case in range(num_cases):
        d, n = input().split()
        d = int(d)
        n = int(n)
        horses = []
        for _ in range(n):
            position, speed = input().split()
            position = int(position)
            speed = int(speed)
            horses.append([position, speed])

        horses.sort(key=lambda x: x[0])
        while len(horses) > 1:
            horse1 = horses.pop()
            horse0 = horses.pop()
            this_time = (d - horse1[0]) / horse1[1]
            last_time = (d - horse0[0]) / horse0[1]
            if this_time > last_time:
                horses.append(horse1)
            else:
                horses.append(horse0)
        horse = horses.pop()
        time = (d - horse[0]) / horse[1]
        our_speed = d / time
        print(output_str.format(case + 1, our_speed))

def main():
    first_attempt()

if __name__ == '__main__':
    main()
