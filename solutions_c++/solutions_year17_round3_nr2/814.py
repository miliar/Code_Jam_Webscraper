#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

const int DAY = 1440;
const int HALF = 720;

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

    int t;
    cin >> t;
    REP(o, t) {
        int c, j, res;
        cin >> c >> j;
        vector<pair<int, int>> tasks(c + j);
        REP(x, c + j) {
            cin >> tasks[x].first >> tasks[x].second;
        }
        sort(tasks.begin(), tasks.end());

        if (c == 0) {
            swap(c, j);
        }
        if (c + j < 2) {
            res = 2;
        } else if (c == 2) {
            if ((tasks[1].second - tasks[0].first <= HALF) || (DAY - tasks[1].first + tasks[0].second <= HALF)) {
                res = 2;
            } else {
                res = 4;
            }
        } else {
            res = 2;
        }

        cout << "Case #" << o + 1 << ": " << res << endl;
    }

	return 0;
}
#endif