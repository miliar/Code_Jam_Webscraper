#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;

int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        int n, q;
        cin >> n >> q;
        vector<int> e(n), s(n);
        vector<vector<int>> edges(n, vector<int>(n));
        FOR(i, 0, n) {
            cin >> e[i] >> s[i];
        }
        FOR(i, 0, n) {
            FOR(j, 0, n) {
                int t;
                cin >> t;
                edges[i][j] = t;
            }
        }
        FOR(i, 0, q) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            vector<double> dp(n);
            dp[v] = 0;
            RFOR(j, v - 1, u) {
                long long accum = 0;
                double minx = DBL_MAX;
                IFOR(k, j+1, v) {
                    accum += edges[k-1][k];
                    if (accum <= e[j]) {
                        minx = min(minx, accum / (double)s[j] + dp[k]);
                    }
                }
                dp[j] = minx;
            }
            printf("%.14f\n", dp[u]);

        }

    }
    return 0;
}