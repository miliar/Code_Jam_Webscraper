# Google 2017 Code Jam, Charlie Crandall
import fileinput

def flip(cakes, pos, k):  # Invert k cakes at pos
    cake_list = list(cakes)
    for i in range(pos, pos + k):
        cake_list[i] = '-' if cake_list[i] == '+' else '+'
    return ''.join(cake_list)

# Return a valid point to flip, -1 for impossible, and len+ for finshed
def find_flip(cakes, k, start_pos=0):  #
    if not cakes.count('-', start_pos):
        return len(cakes) + 1  # signal for finished
    first_blank = cakes.index('-', start_pos)
    return first_blank if first_blank <= len(cakes) - k else -1


with fileinput.input() as f:
    cases = int(f.readline())
    for i in range(1, cases + 1):
        (cakes, k) = f.readline().split()
        k = int(k)
        next_flip = find_flip(cakes, k)
        counter = 0  # Also using the counter to catch my screwups
        while (0 <= next_flip < len(cakes) and counter < len(cakes) * 2):
            counter = counter + 1
            cakes = flip(cakes, next_flip, k)
            next_flip = find_flip(cakes, k, next_flip)
        output = 'IMPOSSIBLE' if next_flip < 0 else str(counter)
        print("Case #{}: {}".format(str(i), output))

