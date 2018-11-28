#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        string s;
        cin >> s;
        int j = 0;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] < s[j]) {
                if (s[j] > '1') {
                    --s[j];
                    for (int k = j + 1; k < s.size(); k++) {
                        s[k] = '9';
                    }
                    break;
                } else {
                    s = string(s.size() - 1, '9');
                    break;
                }
            } else if (s[i] > s[j]) {
                j = i;
            }
        }
        cout << "Case #" << test << ": " << s << '\n';
        cerr << "Solved case " << test << '\n';
    }
    return 0;
}
