#include <bits/stdc++.h>

using namespace std;

#define forn(x, a, b) for (int x = a; x <= b; ++x)
#define for1(x, a, b) for (int x = a; x >= b; --x)
#define sz(a) (int)a.size()

int main() {
    
    int t;
    cin >> t;
    forn(test, 1, t) {
        string s;
        cin >> s;
        int n = sz(s);
        int pos = 0;
        while (pos < n - 1 && s[pos] <= s[pos + 1]) ++pos;
        if (pos == n - 1) {
            cout << "Case #" << test << ": " << s << "\n";
            continue;
        }
        forn(i, pos + 2, n - 1) s[i] = '9';
        for1(i, pos, 0) {
            if (s[i] > s[i + 1]) {
                s[i + 1] = '9';
                s[i]--;
            }
        }
        cout << "Case #" << test << ": ";
        if (s[0] != '0') cout << s[0];
        forn(i, 1, n - 1) cout << s[i];
        cout << "\n";        
    }
    
    return 0;
}