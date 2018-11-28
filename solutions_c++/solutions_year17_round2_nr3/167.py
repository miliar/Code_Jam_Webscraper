#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#define _USE_MATH_DEFINES
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>
#include <iomanip>
#include <unordered_map>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))

#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cerr << "> " << #x << ": " << (x) << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

vector<double> calc(int n, vector<int64> endur, vector<double> v, vector<vector<int64>> dist, vector<int> qb, vector<int> qe) {
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dist[i][j] = mmin(dist[i][j], mplus(dist[i][k], dist[k][j]));
            }
        }
    }
    vector<vector<double>> timed(n, vector<double>(n, -1));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            timed[i][j] = dist[i][j] != -1 && dist[i][j] <= endur[i] ? dist[i][j] / v[i] : -1;
        }
    }
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                timed[i][j] = mmin(timed[i][j], mplus(timed[i][k], timed[k][j]));
            }
        }
    }
    vector<double> result(qb.size());
    for (int i = 0; i < qb.size(); ++i) {
        int u = qb[i] - 1;
        int v = qe[i] - 1;
        result[i] = timed[u][v];
    }
    return result;
}


int main() {
     // freopen("../input.txt", "rt", stdin);
     // freopen("../output.txt", "wt", stdout);

    // start_testing();

    int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n, q;
        cin >> n >> q;
        vector<int64> endur(n);
        vector<double> vel(n);
        for (int i =0 ; i < n; ++i) {
            cin >> endur[i] >> vel[i];
        }
        vector<vector<int64>> dist(n, vector<int64>(n));
        for (int i= 0 ; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> dist[i][j];
            }
        }
        vector<int> qb(q), qe(q);
        for (int i = 0; i < q; ++i) {
            cin >> qb[i] >> qe[i];
        }
        auto res = calc(n, endur, vel, dist, qb, qe);

        printf("Case #%d:", testNumber);
        for (int i = 0; i < q; ++i) {
            printf(" %.8f", res[i]);
        }
        printf("\n");
        // cout << "Case #" << testNumber << ": " << setprecision(6) << res << endl;
    }

    return 0;
}
