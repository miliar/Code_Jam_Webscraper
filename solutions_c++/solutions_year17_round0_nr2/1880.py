#include <bits/stdc++.h>

using namespace std;

string solve() {
    string number;
    cin >> number;

    for (int i = 0; i < number.length() - 1; i++) {
        if (number[i] > number[i + 1]) {
            int first_same_digit = i;
            while (first_same_digit > 0 && number[first_same_digit - 1] == number[first_same_digit]) {
                first_same_digit--;
            }

            for (int j = first_same_digit + 1; j < number.length(); j++) {
                number[j] = '9';
            }

            number[first_same_digit]--;

            break;
        }
    }

    if (number[0] == '0') {
        number = number.substr(1);
    }

    return number;
}

bool is_good(int x) {
    string s = to_string(x);
    for (int i = 0; i < s.length() - 1; i++) {
        if (s[i] > s[i + 1]) {
            return false;
        }
    }

    return true;
}

string solve_naive() {
    int x;
    cin >> x;

    while (!is_good(x)) {
        x--;
    }

    return to_string(x);
}

int main() {
    int t;
    cin >> t;

    for (int c = 1; c <= t; c++) {
        cout << "Case #" << c << ": " << solve() << endl;
    }
}
