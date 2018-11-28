#include <bits/stdc++.h>

using namespace std;

int circ_sub(int c) {
    return --c == 47 ? 57 : c;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        string s;
        cin >> s;
        for (int i = s.length() - 1; i > 0; --i) {
            if (s[i] < s[i - 1]) {
                for (int j = i; j < s.length(); ++j) {
                    s[j] = 57;
                }
                s[i - 1] = circ_sub(s[i - 1]);
            }
        }
        cout << "Case #" << t + 1 << ": ";
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != 48) cout << s[i];
        }
        cout << endl;
    }
    return 0;
}