from parse import *

def main():
    cases = int(input())
    for case in range(cases):
        r = parse('{max_shyness} {people_string}', input())
        people_list = [int(n) for n in r['people_string']]
        required_people = standing_ovation_calculator(people_list)
        print('Case #{}: {}'.format(case+1, required_people))

def standing_ovation_calculator(List):
    people_required = 0
    for (shyness, n) in reversed(list(enumerate(List))):
        existing = shyness + n
        surplus = existing - people_required
        if surplus < 0:
            people_required = shyness - surplus
        else:
            people_required = shyness
    return people_required

if __name__ == '__main__':
    main()
