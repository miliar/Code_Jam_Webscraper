#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        reverse(s.begin(), s.end());
        int tag = 0;
        for (size_t i = 1; i < s.size(); i++) {
            if (s[i] > s[i - 1]) {
                s[i]--;
                tag = i;
            }
        }
        for (int i = 0; i < tag; i++) {
            s[i] = '9';
        }
        while (s.size() > 1 && s.back() == '0') {
            s.pop_back();
        }
        reverse(s.begin(), s.end());
        cout << "Case #" << t << ": " << s << endl;
    }
}
