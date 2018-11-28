#include <iostream>
using namespace std;

long get_tidy_num(string num) {
    long length = num.length(), tidy = 0;
    int prev_digit = 0, cur_digit;
    bool is_digit_switched = false;

    for (int i=0; i<length; ++i) {
        if (is_digit_switched) {
            cur_digit = 9;
        } else {
            cur_digit = num[i] - '0';
        }

        if (cur_digit < prev_digit) {
            char tidy_so_far[18];
            sprintf(tidy_so_far, "%ld", tidy - 1);
            is_digit_switched = true;
            tidy = get_tidy_num(tidy_so_far);
            cur_digit = 9;
        }

        prev_digit = cur_digit;
        tidy = tidy * 10 + cur_digit;
    }

    return tidy;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        string N;
        cin >> N;
        cout << "Case #" << test << ": " << get_tidy_num(N) << endl;
    }

    return 0;
}