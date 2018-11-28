#include <bits/stdc++.h>

using namespace std;

void flip(string& s, int pos, int k) {
    for (size_t j = pos; j < pos + k; ++j) {
        if (s[j] == '-') {
            s[j] = '+';
        } else {
            s[j] = '-';
        }
    }
}

int main() {
    int tests;
    cin >> tests;

    for (int Test = 1; Test <= tests; ++Test) {

        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;

        for (int i = 0; i < int(s.length()) - k + 1; ++i) {
            if (s[i] == '-') {
                flip(s, i, k);
                ++ans;
            }
        }

        bool good = true;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '-') {
                good = false;
            }
        }

        cout << "Case #" << Test << ": ";
        if (good) {
            cout << ans << '\n';
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }

    return 0;
}