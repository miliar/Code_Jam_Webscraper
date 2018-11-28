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

pair<int64, int64> calc(int64 n, int64 k, unordered_map<int64, unordered_map<int64, pair<int64, int64>>>& mem) {
    if (k == 0)
        return make_pair(n, n);
    auto it = mem[n].find(k);
    if (it != mem[n].end())
        return it->second;
    if (n % 2 == 1) {
        return mem[n][k] = calc(n / 2, k / 2, mem);
    } else {
        int64 left = (n - 1) / 2, right = n / 2;
        if (k == 1)
            return mem[n][k] = make_pair(left, right);
        int64 lo = 0, hi = min(left, k - 1) + 1;
        while (lo + 1 < hi) {
            int64 mid = lo + (hi - lo) / 2;
            if (k - 1 - mid < right && calc(right, k - mid, mem) > calc(left, mid, mem) ||
                k - 1 - mid == right && mid != left)
            {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        return mem[n][k] = min(calc(left, lo, mem), calc(right, k - 1 - lo, mem));
    }
}

pair<int64, int64> calc(int64 n, int64 k) {
    unordered_map<int64, unordered_map<int64, pair<int64, int64>>> mem;
    return calc(n, k, mem);
}


int main() {
     freopen("../input.txt", "rt", stdin);
     freopen("../output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int64 n, k;
        cin >> n >> k;
        auto res = calc(n, k);
        // printf("Case #%d: %.7f\n", testNumber, res);
        cout << "Case #" << testNumber << ": " << res.second << " " << res.first << endl;
    }

    return 0;
}
