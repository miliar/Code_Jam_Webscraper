#include <bits/stdc++.h>

using namespace std;
using ll = long long;
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define REP(i, n)    FOR(i, 0, n - 1)

int T, m;
string s;

int comp(string s) {
    int res = 0;
    int n = s.length();

    REP(i, n - m + 1) {
        if (s[i] == '-') {
            FOR(j, i, i + m - 1) {
                s[j] = (s[j] == '-') ? '+' : '-';
            }
            res++;
        }
    }
    REP(i, n) {
        if (s[i] == '-') {
            res = n + 1;
            break;
        }
    }

    return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> T;
    REP(t, T) {
        cin >> s >> m;

        int res = comp(s);
        reverse(begin(s), end(s));
        res = min(res, comp(s));

        cout << "Case #" << t + 1 << ": ";

        if (res > s.length()) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << res << "\n";
        }
    }

    fclose(stdout);
}

