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
        int n, k, cnt = 0;
        cin >> s >> k;
        n = sz(s);
        bool ok = 1;
        forn(i, 0, n - 1) {
            if (s[i] == '-') {
                if (i + k - 1 >= n) {
                    ok = 0;
                    break;
                }
                ++cnt;
                forn(j, i, i + k - 1) s[j] = (s[j] == '-' ? '+' : '-');
            }
        }
        cout << "Case #" << test << ": ";
        if (ok) cout << cnt << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    
    return 0;
}