#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        string s;
        cin >> s;
        int n = s.size(), k, ans = 0;
        cin >> k;
        forn (i, n - k + 1) {
            if (s[i] == '-') {
                ++ans;
                forn (j, k) {
                    s[i + j] = s[i + j] == '+' ? '-' : '+';
                }
            }
        }
        bool was = false;
        forn (i, k - 1) {
            if (s[n - k + 1 + i] == '-') {
                was = true;
            }
        }
        if (was) {
            cout << "Case #" << q + 1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << q + 1 << ": " << ans << endl;
        }
    }
}
