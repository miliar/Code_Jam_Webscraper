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
        int64 n;
        cin >> n;
        string str = to_string(n);
        n = str.size();
        bool tiny = false;
        while(!tiny) {
            int last = 0;
            tiny = true;
            REP(x, n) {
                int i = str[x] - '0';
                if (i < last) {
                    str[x - 1]--;
                    FOR(y, x, n) {
                        str[y] = '9';
                    }
                    tiny = false;
                    break;
                }
                last = i;
            }
        }

        cout << "Case #" << o + 1 << ": " << stoll(str) << endl;
    }

	return 0;
}
#endif