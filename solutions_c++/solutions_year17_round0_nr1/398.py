#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int casenum = 1; casenum <= T; ++casenum) {
        string ps;
        int l, n = 0;
        cin >> ps >> l;
        forn(i, ps.size() - l + 1) {
            //cout << ps << endl;
            if (ps[i] == '-') {
                ++n;
                forn(j, l) {
                    ps[i+j] = ps[i+j] == '-' ? '+' : '-';
                }
            }
        }
        forn(i, ps.size()) {
            if (ps[i] == '-') n = -1;
        }
        cout << "Case #" << casenum << ": ";
        if (n == -1) cout << "IMPOSSIBLE";
        else cout << n;
        cout << endl;
    }
    return 0;
}

