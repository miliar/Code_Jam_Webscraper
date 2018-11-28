#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

    int t;
    cin >> t;
    REP(o, t) {
        string s;
        cin >> s;
        int n = s.size(), k;
        cin >> k;

        int res = 0;
        REP(x, n - k + 1) {
            if (s[x] == '-') {
                REP(y, k) {
                    s[x + y] = s[x + y] == '-' ? '+' : '-';
                }
                res++;
            }
        }

        cout << "Case #" << o + 1 << ": ";
        REP(x, n) {
            if (s[x] == '-') {
                res = INF;
                break;
            }
        }
        if (res != INF) {
            cout << res << endl;
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }

	return 0;
}
#endif