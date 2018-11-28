#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<ld, ld> point;

const int N = (int)(1e3) + 7;
const int M = (int)(1e5) + 7;
const ld eps = 1e-12;
const ll MOD = (ll)(1e9) + 7;
const ll INF = (ll)(1e9) + 7;

pii a[N];
ll dp[N][N];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    //freopen("library.in", "r", stdin);
    //freopen("library.out", "w", stdout);
    int ttt;
    cin >> ttt;
    for (int iii = 1; iii <= ttt; ++iii) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> a[i].x >> a[i].y;
        }
        sort(a, a + n);
        reverse(a, a + n);
        for (int i = 0; i <= n; ++i)
            for (int j = 0; j <= k; ++j)
                dp[i][j] = 0;
        for (int i = 0; i < n; ++i) {
            dp[i][1] = 2LL * a[i].x * a[i].y + 1LL * a[i].x * a[i].x;
            for (int j = 1; j < k; ++j) {
                for (int q = 0; q < i; ++q) {
                    dp[i][j + 1] = max(dp[i][j + 1], dp[q][j] + 2LL * a[i].x * a[i].y);
                }
            }
        }
        ll sum = 0;
        for (int i = 0; i < n; ++i)
            sum = max(sum, dp[i][k]);
        printf("Case #%d: %1.20lf\n", iii, (double)(sum * M_PI));
    }
    return 0;
}
