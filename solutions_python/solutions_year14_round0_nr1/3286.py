#!/usr/bin/env python3

def discover_card_trick(row1, row2):
    x = set(row1) & set(row2)
    if len(x) == 1: return list(x)[0]
    elif len(x) == 0: return "Volunteer cheated!"
    elif len(x) > 1: return "Bad magician!"


def main():
    for n in range(int(input())):
        x = int(input())
        rows1 = list()
        for i in range(4):
            rows1.append([int(x) for x in input().split()])
        
        y = int(input())
        rows2 = list()
        for i in range(4):
            rows2.append([int(x) for x in input().split()])
        
        print("Case #{0}: {1}".format(n+1, discover_card_trick(rows1[x-1], rows2[y-1])))
    
if __name__ == '__main__':
    main()
