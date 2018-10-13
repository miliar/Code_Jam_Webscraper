#!/usr/bin/python


def pancakes_(pancakes):
    p = []
    for s in pancakes:
        if s == '+':
            p.append(0)
        elif s == '-':
            p.append(1)
        else:
            raise Exception("problem with input")
    return p

def reverse_pancakes(pancakes, index, k):
    for i in range (index, index+k):
        pancakes[i] = (pancakes[i] + 1 )%2
    return pancakes

def min_reverse_flip(pancakes, k):
    step = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == 1:
            reverse_pancakes(pancakes, i, k)
            i = i + k 
            step = step + 1
    return step

def happy(pancakes):
    return [0 for i in range(len(pancakes))]


if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        input_ = raw_input("")
        pancakes, k = str.split(input_," ")
        k = int(k)
        p = pancakes_(pancakes)
        step = min_reverse_flip(p, k)
        if p == happy(pancakes):
            print "CASE #{}: {}".format(test+1, step)
        else:
            print "CASE #{}: IMPOSSIBLE".format(test+1)
        