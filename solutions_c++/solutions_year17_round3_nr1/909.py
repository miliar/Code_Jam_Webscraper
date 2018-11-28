#include <vector>
#include <map>
#include <set>
#include <complex>
#include <ctime>
#include <iostream>
#include <cmath>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cassert>
#include <sstream>

const long double PI(acosl(-1.0));
const long double E = 2.71828182845904;
long double eps = 1e-10;

#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define sqr(x) ((x)*(x))
#define F first
#define S second
#define inf (int)(1e9+7)
#define infll (ll)(1e18+3)
#define sz(x) ((int)x.size())
#define bits(x) __builtin_popcount(x)
#define bitsl(x) __builtin_popcountll(x)

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef vector <ll > vll;
typedef vector<int> vi;
typedef pair < ll, ll > pll;
typedef pair < int, int > pii;
typedef vector<vi> vii;
typedef int huint;

using namespace std;

const int N = 1050;

ld calc(ld r, ld h) {
    ld s = 2 *  r * h ;
    s +=  r * r ;
    return s;
}

bool comp(pair<ld, ld> &a, pair<ld, ld> &b) {
    return a.F > b.F;
}
vector<vector<ld>> dp(N);

int main() {
    freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
    for(int i(0);i<N;i++)
        dp[i].resize(N);

    int test;
    cin >> test;
    for (int tt(1);tt <=test; tt++) {
        int n,k;
        cin >> n >> k;
        for (int i(0);i<=n;i++)
            for (int j(0);j<=k;j++)
                dp[i][j] = -1;
        vector<pair<ld, ld>> p(n);
        for (int i(0);i<n;i++){
            cin >> p[i].F >> p[i].S;
        }
        sort(all(p), comp);
        dp[0][0] = 0;
        for (int i(0);i<n;i++){
            for (int j(0);j<k;j++) {
                if (dp[i][j] == -1) continue;
                ld s = dp[i][j];
                if (j == 0) s += p[i].F * p[i].F;
                s += p[i].F * p[i].S * 2;
                dp[i + 1][j + 1] = max(s, dp[i + 1][j + 1]);
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j]);
            }
            dp[i + 1][k] = max(dp[i][k], dp[i + 1][k]);
        }
        cout.precision(10);
        cout << "Case #" << tt << ": ";
        cout << fixed << dp[n][k] * PI << "\n";
    }
}
