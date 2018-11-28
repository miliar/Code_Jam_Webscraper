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


double calc(int d, int n, vi& pos, vi& v) {
    double max_time = 0;
    for (int i =0 ; i < n; ++i) {
        max_time = max(max_time, double(d - pos[i]) / v[i]);
    }
    return d / max_time;
}


int main() {
     // freopen("../input.txt", "rt", stdin);
     // freopen("../output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int d;
        int n;
        cin >> d >> n;
        vector<int> pos(n), v(n);
        for (int i=  0; i < n; ++i) {
            cin >> pos[i] >> v[i];
        }
        auto res = calc(d, n, pos, v);
        // printf("Case #%d: %.7f\n", testNumber, res);
        printf("Case #%d: %.6f\n", testNumber, res);
        // cout << "Case #" << testNumber << ": " << setprecision(6) << res << endl;
    }

    return 0;
}
