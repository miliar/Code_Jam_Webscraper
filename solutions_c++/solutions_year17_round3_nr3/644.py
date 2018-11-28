#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

bool is_zero(double x) {
    return x >= -EPS && x <= EPS;
}

bool all_the_same(vector<double>& ais) {
    REP(x, ais.size() - 1) {
        if (!is_zero(ais[x] - ais[x + 1])) {
            return false;
        }
    }
    return true;
}

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
        double u;
        cin >> u;
        vector<double> ais;
        REP(x, n) {
            double ai;
            cin >> ai;
            ais.push_back(ai);
        }
        if (n == 1) {
            ais[0] += u;
        } else {
            // while (u > EPS) {
            //     if (all_the_same(ais)) {
            //         u /= n;
            //         REP(x, n) {
            //             ais[x] += u;
            //         }
            //         break;
            //     }

            //     int a_i = 0;
            //     REP(x, n) {
            //         if (ais[x] < ais[a_i]) {
            //             a_i = x;
            //         }
            //     }
            //     int b_i = -1;
            //     REP(x, n) {
            //         if (ais[x] > ais[a_i]) {
            //             if (b_i == -1) {
            //                 b_i = x;
            //             } else if (ais[x] < ais[b_i]) {
            //                 b_i = x;
            //             }
            //         }
            //     }
                
            //     double d = ais[b_i] - ais[a_i];
            //     d = min(d, u);
            //     ais[a_i] += d;
            //     u -= d;
            // }

            while (u > EPS) {
                int a_i = 0;
                REP(x, n) {
                    if (ais[x] < ais[a_i]) {
                        a_i = x;
                    }
                }
                int b_i = -1;
                vector<int> mins;
                REP(x, n) {
                    if (is_zero(ais[x] - ais[a_i])) {
                        mins.push_back(x);
                    } else {
                        if (b_i == -1) {
                            b_i = x;
                        } else if (ais[x] < ais[b_i]) {
                            b_i = x;
                        }
                    }
                }

                if (mins.size() == n) {
                    u /= n;
                    REP(x, n) {
                        ais[x] += u;
                    }
                    break;
                }
                double d = ais[b_i] - ais[a_i];
                double dd = min(u, mins.size() * d);
                d = dd / mins.size();
                for (auto it : mins) {
                    ais[it] += d;
                }
                u -= dd;
            }
        }
        double res = 1.0;
        REP(x, n) {
            res *= ais[x];
        }
        cout << "Case #" << o + 1 << ": " << res << endl;
    }

	return 0;
}
#endif