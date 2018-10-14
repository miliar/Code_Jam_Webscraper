import os


def main():
    with open('A-small-attempt0.in') as f:
        num_cases = int(f.readline())
        for case in range(1, num_cases+1):
            r1 = int(f.readline())
            array = []
            for i in range(4):
                array.append([int(x) for x in f.readline().split()])
            possible = set(array[r1-1])

            r2 = int(f.readline())

            array = []
            for i in range(4):
                array.append([int(x) for x in f.readline().split()])
            
            possible = set(array[r2-1]).intersection(possible)

            answer = None 
            if len(possible) > 1:
                answer = 'Bad magician!'
            elif len(possible) == 0:
                answer = 'Volunteer cheated!'
            else:
                answer = next(iter(possible))
                
            print ('Case #{0}: {1}'.format(case, answer))

if __name__ == "__main__":
    main()