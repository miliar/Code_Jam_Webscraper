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

int calc(string& s, int k) {
    int n = s.length();
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '-') {
            if (i + k <= n)
            {
                for (int j = 0; j < k; ++j)
                {
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
                }
                ++res;
            } else {
                return -1;
            }
        }
    }
    return res;
}


int main() {
     // freopen("input.txt", "rt", stdin);
    // freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        string s;
        int k;
        cin >> s >> k;
        auto res = calc(s, k);
        // printf("Case #%d: %.7f\n", testNumber, res);
        cout << "Case #" << testNumber << ": ";
        if (res >= 0)
            cout << res;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}
