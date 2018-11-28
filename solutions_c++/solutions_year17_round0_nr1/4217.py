#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int flipping(int p_count, string p_row, int p_flipper_size);
string flipK(string p_row, int p_flipper_size);

int main() {
    int num_inputs;
    cin >> num_inputs;

    for (int i = 0; i < num_inputs; i++) {
        string cake_row;
        int flipper_size;
        int flip_count = 0;

        cin >> cake_row >> flipper_size;
        //cout << cake_list << " " << flipper_size << endl;
        flip_count = flipping(flip_count, cake_row, flipper_size);
        if (flip_count >= 0) {
            cout << "Case #" << i+1 << ": " << flip_count << endl;
        } else {
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

int flipping(int p_count, string p_row, int p_flipper_size) {
    int row_size = p_row.size();
    // If there are fewer than K cakes left,
    // check if they are all facing up:
    // 1) if NOT all facing up, mission impossible, return -1
    // 2) if all facing up, succeed, return flip count
    if (row_size < p_flipper_size) {
        for (int i = 0; i < row_size; i++) {
            if (p_row[i] == '-') {
                return -1;
            }
        }
        return p_count;
    }

    // Check if the first cake is facing up:
    // 1) if facing up, remove it from the row
    // 2) if NOT facing up, flip K cakes, increase flip count
    if (p_row[0] == '+') {
        p_row.erase(p_row.begin());
        p_count = flipping(p_count, p_row, p_flipper_size);
    } else {
        p_row = flipK(p_row, p_flipper_size);
        p_count = flipping(p_count+1, p_row, p_flipper_size);
    }
    return p_count;
}

string flipK(string p_row, int p_flipper_size) {
    string new_row;
    new_row = p_row;
    for (int i = 0; i < p_flipper_size; i++) {
        if (new_row[i] == '+') {
            new_row[i] = '-';
        } else if (new_row[i] == '-') {
            new_row[i] = '+';
        } else {
            cout << "ERROR: unexpected string!" << endl;
            assert(false);
        }
    }
    return new_row;
}
