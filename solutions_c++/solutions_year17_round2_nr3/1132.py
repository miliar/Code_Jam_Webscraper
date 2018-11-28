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

const int N = (int)(1e2) + 7;
const int M = (int)(32);
const ld eps = 1e-12;
const ll MOD = (ll)(1e9) + 7;
const ll INF = (ll)(1e9) + 7;

int a[N], s[N];
int d[N][N];
ld dp[N];

void solve(int iii) {
    cout << "Case #" << iii << ": ";
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> s[i];
    }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> d[i][j];
    int ss, f;
    cin >> ss >> f;
    for (int i = 0; i < N; ++i)
        dp[i] = 1e18;
    dp[0] = 0.0;
    for (int i = 0; i < n; ++i) {
        if (dp[i] < 1e18 + eps) {
            int j = i + 1;
            ll cur = 0;
            while (j < n && cur + d[j - 1][j] <= a[i]) {
                cur += d[j - 1][j];
                dp[j] = min(dp[j], dp[i] + 1.0 * cur / s[i]);
                ++j;
            }
        }
    }
    printf("%1.20lf\n", (double)dp[n - 1]);
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    //freopen("brackets.in", "r", stdin);
    //freopen("brackets.out", "w", stdout);
    int ttt;
    cin >> ttt;
    for (int i = 0; i < ttt; ++i) {
        solve(i + 1);
    }
    return 0;
}
