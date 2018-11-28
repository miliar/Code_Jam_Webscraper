#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        string s;
        int k;
        cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i <= s.length() - k; ++i) {
            if (s[i] == '-') {
                ++cnt;
                for (int j = i; j < i + k; ++j) {
                    s[j] = (s[j] == '-') ? '+' : '-';
                }
            }
        }
        bool remaining = false;
        for (int i = 0; i < k; ++i) {
            if (s[s.length() - (i + 1)] == '-') {
                remaining = true;
                break;
            }
        }
        cout << ("Case #" + to_string(c) + ": ") + (!remaining ? to_string(cnt) : "IMPOSSIBLE") << endl;
    }
    return 0;
}