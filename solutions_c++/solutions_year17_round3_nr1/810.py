#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

struct Pancake {
    int r, h;
};

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
    cout << fixed << setprecision(10);

    int t;
    cin >> t;
    REP(o, t) {
        int n, k;
        cin >> n >> k;
        vector<Pancake> pancakes(n);
        vector<double> heights;
        REP(x, n) {
            cin >> pancakes[x].r >> pancakes[x].h;
        }
        double result = 0;
        REP(x, n) {
            heights.clear();
            double res = (double)pancakes[x].r * (double)pancakes[x].r + 2.0 * (double)pancakes[x].r * (double)pancakes[x].h;
            REP(y, n) {
                if (x != y && pancakes[x].r >= pancakes[y].r) {
                    heights.push_back(2.0 * (double)pancakes[y].r * (double)pancakes[y].h);
                }
            }
            if (heights.size() >= k - 1) {
                sort(heights.begin(), heights.end());
                reverse(heights.begin(), heights.end());
                REP(y, k - 1) {
                    res += heights[y];
                }
                result = max(result, res);
            }
        }
        cout << "Case #" << o + 1 << ": " << M_PI * result << endl;
    }
	return 0;
}
#endif