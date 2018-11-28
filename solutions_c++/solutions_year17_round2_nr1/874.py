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

    cout << fixed << setprecision(10);

    int t;
    cin >> t;
    REP(o, t) {
        int d, n;
        cin >> d >> n;
        vector<pair<int, int>> horses(n);
        REP(x, n) {
            cin >> horses[x].first >> horses[x].second;
        }
        sort(horses.begin(), horses.end());
        double finish = 0;
        for (int x = n - 1; x >= 0; --x) {
            double t = (double)(d - horses[x].first) / (horses[x].second);
            finish = max(finish, t);
        }
        cout << "Case #" << (o + 1) << ": " << d / finish << endl;
    }

	return 0;
}
#endif