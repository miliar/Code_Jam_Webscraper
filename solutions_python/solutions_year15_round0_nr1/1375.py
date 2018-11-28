def solve(shy_people):
    num_clapped = 0
    additional_people = 0
    for shyness_level in range(len(shy_people)):
        if shyness_level > num_clapped:
            additional_people += shyness_level - num_clapped
            num_clapped = shyness_level 
        num_clapped += shy_people[shyness_level]
    return additional_people

def answer(outputs):
    for i, output in enumerate(outputs):
        print 'Case #{0}: {1}'.format(i+1, output)
    
def main():
    num_samples = input()
    outputs = []
    for _ in range(num_samples):
        data = raw_input().rstrip().split()
        max_shyness = int(data[0])
        shy_people = map(int, data[1])
        additional_people = solve(shy_people)
        outputs.append(additional_people)
    answer(outputs)

main()
