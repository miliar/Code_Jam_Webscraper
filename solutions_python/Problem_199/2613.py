"""
    FLIP IT
    Case #1: ---+-++- 3 -> 3
    Case #2: +++++ 4 -> 0
    Case #3: -+-+- 4 -> IMPOSSIBLE
"""
def main():
    """Main
    Start with this main function
    """
    # Pancake flipper
    total_line = int(input())
    for i in range(1, total_line+1):
        pancake_row, flipper_width = [s for s in input().split(" ")]
        flipper_width = int(flipper_width)
        ans = is_flipable(pancake_row, flipper_width)
        print('Case #{}: {}'.format(i, str(ans)))

def is_flipable(pancake_row, flipper_width):
    """is_flipable
    Check is it possible to flip pancakes with oversized pancake flipper
    Args:
        pancake_row: Represents the row of pancakes
        flipper_width: Size of flipper
    Returns: Minimum number of times to flip or IMPOSSIBLE
    Raises:
    """
    flip_times = 0
    index_marker = -1
    while True:
        m_index = pancake_row.find('-')
        if len(pancake_row) - flipper_width < m_index or len(pancake_row) - flipper_width <= index_marker:
            break
        if m_index != -1:
            pancake_row = pancake_row[:m_index] + ''.join('+' if c == '-' else '-' for c in pancake_row[m_index:m_index+flipper_width]) + pancake_row[m_index+flipper_width:]
            index_marker = m_index
            flip_times += 1
        else:
            index_marker += 1

    blank_pos = pancake_row.find('-')
    if blank_pos == -1:
        return str(flip_times)
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    main()
