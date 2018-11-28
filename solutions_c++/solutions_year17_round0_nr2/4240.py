#include <bits/stdc++.h>

using namespace std;

int main () {
    int tt; 
    cin >> tt;
    for (int cases = 1; cases <= tt; ++cases) {
        cout << "Case #" << cases << ": ";
        string s; 
        cin >> s;
        int n = s.length();
        char m = '9';
        for (int i = n-1; i >= 0; --i) {
            m = min(m, s[i]);
            if (m < s[i]) {
                m = (s[i] = s[i] - 1);
                for (int j = i+1; j < n; ++j)
                    s[j] = '9';
            }
        }
        cout << stoll(s) << "\n";
    }
}
