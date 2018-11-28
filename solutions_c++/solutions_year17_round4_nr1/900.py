#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

const int INF = 1e9;

int main () {
    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    cout.setf(std::ios_base::fixed);
    cout.precision(24);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int tt;
    cin >> tt;
    vector < vector < vector < vector < int > > > > dp;
    for (int t = 0; t < tt; ++t) {
        cout << "Case #" << t + 1 << ": ";
        dp.assign(4, vector < vector < vector < int > > >
                (110, vector < vector < int > > (110, vector < int > (110, -INF))));
        int n, p;
        cin >> n >> p;
        vector < int > start(3);
        int add = 0;
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            int a;
            cin >> a;
            if (a % p == 0) {
                add++;
            } else {
                start[ (a % p) - 1]++;
                sum++;
            }
        }
        dp[0][start[0]][start[1]][start[2]] = 0;
        for (int s = sum; s >= 0; --s) {
            for (int ost = 0; ost < p; ++ost) {
                for (int i = 0; i <= s; ++i) {
                    for (int j = 0; j + i <= s; ++j) {
                        for (int k = 0; j + i + k <= s; ++k) {
                            if (i > 0) {
                                dp[ (ost + 1) % p ][i - 1][j][k] = max(dp[ (ost + 1) % p ][i - 1][j][k],
                                                                       dp[ost][i][j][k] + (ost == 0));
                            }
                            if (j > 0) {
                                dp[ (ost + 2) % p ][i][j - 1][k] = max(dp[ (ost + 2) % p ][i][j - 1][k],
                                                                       dp[ost][i][j][k] + (ost == 0));
                            }
                            if (k > 0) {
                                dp[ (ost + 3) % p ][i][j][k - 1] = max(dp[ (ost + 3) % p ][i][j][k - 1],
                                                                       dp[ost][i][j][k] + (ost == 0));
                            }
                        }
                    }
                }
            }
        }
        int res = 0;
        for (int ost = 0; ost < p; ++ost) {
            res = max(res, dp[ost][0][0][0]);
        }
        cout << res + add << "\n";
        cerr << "done " << tt + 1 << endl;
    }
    return 0;
}


