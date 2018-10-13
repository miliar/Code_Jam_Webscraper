#!/usr/bin/env python3

T = int(input())

def characters_counts(string):
    current = None
    characters = list()
    counts = list()
    for c in string:
        if c != current:
            if current != None:
                characters.append(current)
                counts.append(count)
            current = c
            count = 1
        else:
            count += 1
    characters.append(current)
    counts.append(count)
    return characters, counts


for case in range(T):
    N = int(input())

    the_characters = None

    fegla_won = False

    all_counts = list()

    for i in range(N):
        string = input()

        characters, counts = characters_counts(string)

        if the_characters is None:
            the_characters = characters
        else:
            if the_characters != characters:
                fegla_won = True
                continue

        all_counts.append(counts)

    if fegla_won:
        print("Case #{0}: Fegla Won".format(case+1))
        continue
        
    #print(characters)
    #print(all_counts)
    delta = 0
    for l in zip(*all_counts):
        #print(l)
        l = sorted(l)
        median = l[len(l)//2]
        #print(median)
        delta += sum(abs(i-median) for i in l)
    print("Case #{0}: {1}".format(case+1, delta))
