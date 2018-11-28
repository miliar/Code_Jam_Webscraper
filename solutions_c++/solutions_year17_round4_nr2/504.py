#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
        int tests; cin >> tests;
        for(int test = 0; test<tests; ++test) {
                int n, c, m;
                cin >> n >> c >> m;
                vector<vector<int> > seats(n);
                vector<vector<int> > counts(n);
                vector<int> totals(n);
                for(int i = 0; i<n; ++i) {
                        totals[i] = 0;
                        for(int j = 0; j<c; ++j)
                                counts[i].push_back(0);
                }
                int tp, tb;
                int maxp = 0;
                for(int i = 0; i<m; ++i) {
                        cin >> tp >> tb;
                        seats[tp-1].push_back(tb-1);
                        counts[tp-1][tb-1]++;
                        totals[tp-1]++;
                        maxp = max(maxp, tp-1);
                }

                for(int i = 0; i<=maxp; ++i) {
                        sort(seats[i].begin(), seats[i].end());
                }

                int rides = 0;
                int total = 0;
                int running[c];
                for(int i  =0; i<c; ++i){running[i] = 0;}
                for(int i = 0; i<=maxp; ++i) {
                        int mx1 = 0;
                        for(int j = 0; j<c; ++j) {
                                running[j] += counts[i][j];
                                total += counts[i][j];
                        }
                        for(int j = 0; j<c; ++j) {
                                mx1 = max(mx1, running[j]);
                        }

                        int mx2 = (total / (i+1)) + (total % (i+1) != 0);

                        rides = max(mx1, mx2);
                }

                int dp[maxp+1];
                for(int i = 0; i<=maxp; ++i) {
                        dp[i] = 0;
                        if(i != 0) {dp[i] = dp[i-1];}
                        dp[i] += max(0, totals[i] - rides);
                }

                cout << fixed << setprecision(24) << "Case #" << test+1 << ": " << rides << " " << dp[maxp] << endl;
        }
}
