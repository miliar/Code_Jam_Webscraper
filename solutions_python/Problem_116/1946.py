def count_elem (inp_array, empty_symbol):
    return inp_array.count (empty_symbol)

def test_array (inp_array, wildcard, empty):
    # Board is 4x4
    if (len (inp_array) != 4):
        return False

    elem_count = 0
    first_elem_aux_list = [elem for elem in inp_array if (elem != wildcard and elem != empty)]
    if len (first_elem_aux_list) > 0:
        elem_count = count_elem (inp_array, first_elem_aux_list[0])
    wildcard_count = count_elem (inp_array, wildcard)
    empty_count = count_elem (inp_array, empty)

    # Win if 4 non empty symbols of a same player or  3 symbols and a wildcard
    return (((elem_count == 4) or ((elem_count == 3) and (wildcard_count == 1))) and (empty_count == 0))

input_filename = "A-large.in"
output_filename = "A-large_output.txt"

input_file = open (input_filename, "r")
output_file = open (output_filename, "w")

# Read number of test cases
t = int (input_file.readline ().strip ())

# Read T inputs
for test_case in range (t):
    input_matrix = []
    win_player = ""
    sw_wins = False
    sw_empty_elem = False

    # Read each line of the matrix

    for elem in range (4):
        current_row = list (input_file.readline ().strip ())
        input_matrix.append (current_row)

    # Test rows
    # Test null values
    for row in input_matrix:
        sw_wins = test_array (row, 'T', '.')
        if not(sw_empty_elem):
            sw_empty_elem = (count_elem (row, '.') > 0)

        if sw_wins:
            win_player = [elem for elem in row if (elem != 'T' and elem != '.')][0]
            break

    # Test cols
    if not (sw_wins):
        cols_matrix = [[row[i] for row in input_matrix] for i in range (4)]
        for row in cols_matrix:
            sw_wins = test_array (row, 'T', '.')

            if sw_wins:
                win_player = [elem for elem in row if (elem != 'T' and elem != '.')][0]
                break

    # Test diags
    if not (sw_wins):
        diags = [[input_matrix[i][i] for i in range (4)], [input_matrix[4 - i - 1][i] for i in range (4)]]

        for row in diags:
            sw_wins = test_array (row, 'T', '.')

            if sw_wins:
                win_player = [elem for elem in row if (elem != 'T' and elem != '.')][0]
                break

    # Write output
    if sw_wins:
        output_file.write ("Case #" + str (test_case + 1) + ": " + win_player + " won" + "\n")
    elif sw_empty_elem:
        output_file.write ("Case #" + str (test_case + 1) + ": " + "Game has not completed" + "\n")
    else:
        output_file.write ("Case #" + str (test_case + 1) + ": " + "Draw" + "\n")

    # Read a white line between each test case
    input_file.readline ()

input_file.close ()
output_file.close ()
