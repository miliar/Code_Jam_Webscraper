#include <iostream>
#include <cassert>

using namespace std;

typedef unsigned long long ull;

ull lastTidy(ull p_number);
bool isTidy(ull &p_number);

int main() {
    int num_inputs;
    cin >> num_inputs;

    for (int i = 0; i < num_inputs; i++) {
        ull number;
        ull last_tidy;

        cin >> number;
        //cout << number << endl;
        last_tidy = lastTidy(number);
        cout << "Case #" << i+1 << ": " << last_tidy << endl;
    }
    return 0;
}

ull lastTidy(ull p_number) {
    ull count_down = p_number;

    while(1) {
        if (isTidy(count_down)) {
            return count_down;
        }
    }
}

// A number is tidy if the digits are in decreasing order
// from right to left. So start with the righmost digit,
// and checking leftwards one by one.
bool isTidy(ull &p_number) {
    ull new_number = p_number;
    int checkmark_digit = 9; // to make sure number is decreasing from right to left
    int right_shift = 0; // number of right shifts (base 10)
    bool is_tidy = true;
    for (;;) {
        int rightmost_digit = new_number%10;
        if (rightmost_digit <= checkmark_digit) {
            // record the smallest digit ever seen
            checkmark_digit = rightmost_digit;
            if (new_number < 10) {
                break;
            }
            new_number = new_number/10;
            right_shift++;
        } else {
            // number is not tidy, update the number
            new_number -= 1;
            for (int i = 0; i < right_shift; i++) {
                new_number = (new_number * 10) + 9;
            }
            p_number = new_number;
            is_tidy = false;
            break;
        }
    }
    return is_tidy;
}

