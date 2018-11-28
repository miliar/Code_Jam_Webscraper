from collections import defaultdict

fi = open('small.in')
fi = open('A-small-attempt0.in')
fi = open('large.in')
fi = open('A-large.in')
fo = open('aresult.out', 'w')

T = int(fi.readline())

def process_text(text):
    letter_count = defaultdict(lambda: 0)
    number_count = defaultdict(lambda: 0)

    for ch in text:
        letter_count[ch] += 1

    marked_char = ['Z', 'W', 'U', 'X', 'F', 'V', 'R', 'O', 'G', 'I']
    marked_number = [0, 2, 4, 6, 5, 7, 3, 1, 8, 9]
    full_text = ['ZERO', 'TWO', 'FOUR', 'SIX', 'FIVE', 'SEVEN', 'THREE', 'ONE', 'EIGHT', 'NINE']

    for i in range(10):
        char = marked_char[i]
        number = marked_number[i]
        text = full_text[i]

        time = letter_count.get(char, 0)
        if time > 0:
            number_count[number] += time

            for ch in text:
                letter_count[ch] -= time

    sorted_key = sorted(number_count.keys())
    output_val = ''
    for num in sorted_key:
        times = number_count[num]
        for i in range(times):
            output_val = output_val + str(num)
    return output_val

for t in range(1, T+1):
    text = fi.readline().strip()

    output_val = process_text(text)

    fo.write('Case #%i: %s\n' % (t, output_val))