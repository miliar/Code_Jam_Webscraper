#include <iostream>
#include <string>

using namespace std;

char opposite_character(char c) {
    if (c == '-') {
        return '+';
    } else {
        return '-';
    }
}

// inverts characters with indexes in [l, r)
void invert(string &s, int l, int r) {
    for (int i = l; i < r; ++i) {
        s[i] = opposite_character(s[i]);
    }
}

int main() {
    int number_of_cases;
    cin >> number_of_cases;
    for (int test_case = 0; test_case < number_of_cases; ++test_case) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i < 1 - k + (int)s.size(); ++i) {
            if (s[i] == '-') {
                invert(s, i, i + k);
                ++ans;
            }
        }
        for (int i = 1 - k + (int)s.size(); i < (int)s.size(); ++i) {
            if (s[i] == '-') {
                ans = -1;
                break;
            }
        }
        cout << "Case #" << test_case + 1 << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}
