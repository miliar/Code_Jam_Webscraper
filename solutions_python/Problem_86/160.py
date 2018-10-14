#!/usr/bin/env python

def find_note(l, h, notes):
    for t in range(l, h+1):
        if check_note(t, notes):
            return t
    return 'NO'

def check_note(n, notes):
    for note in notes:
        if note % n != 0 and n % note != 0:
            return False
    return True

def main():
    cases = input()
    results = []
    for c in range(cases):
        inp = raw_input()
        inp = inp.split()
        inp = map(int, inp)
        l = inp[1]
        h = inp[2]
        notes = raw_input()
        notes = notes.split()
        notes = map(int, notes)
        results.append(find_note(l, h, notes))
    for c in range(cases):
        print ''.join(['Case #', str(c+1), ': ', str(results[c]) ])
        
if __name__ == '__main__':
    main()