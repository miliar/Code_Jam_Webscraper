#!/usr/bin/python

def standing_ovation(maximum_shyness, frequencies):
    if len(frequencies)!=maximum_shyness+1:
        raise Exception("Frequencies does not match maximum_shyness")
    people_so_far = 0
    people_added = 0
    for i, x in enumerate(frequencies):
        #print(i, x, people_so_far, people_added)
        people_this_level = int(x)
        if people_so_far < i:
            people_added += 1
            people_so_far += 1
        people_so_far += people_this_level
    return str(people_added)

def main():
    with open('input.in', 'r') as f:
        with open('output.txt', 'w') as o:
            n = int(f.readline().rstrip('\n'))
            for i in range(n):
                maximum_shyness, frequencies = f.readline().rstrip('\n').split(' ')
                result = "Case #" + str(i + 1) + ": " + standing_ovation(int(maximum_shyness), frequencies)
                print(result)
                o.write(result + "\n")

if __name__=="__main__":
    main()
