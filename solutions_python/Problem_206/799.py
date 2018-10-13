"""Google codejam"""

def annie_speed(destination):
    """Annie's speed"""
    start, speed = [int(x) for x in input().split()]
    return destination/((destination - start)/speed)

def main():
    """Main Method"""
    cases = int(input())
    for case in range(1, cases+1):
        destination, num_horses = tuple(int(x) for x in input().split())

        slowest = min(annie_speed(destination) for _ in range(num_horses))
        print(f'Case #{case}: {slowest}')


if __name__ == '__main__':
    main()
