#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 1006, inf = 1000111222;
const ld pi = acos(-1);

ld dp[max_n][max_n];
bool vis[max_n][max_n];
vector<pair<int, int> > v;

int n, k;
ld f(int cur, int left) {
    if (left == 0) {
        return 0;
    }
    if (cur == n) {
        return -1;
    }
    if (vis[cur][left]) {
        return dp[cur][left];
    }
    ld ans1, ans2;
    ld f1 = f(cur + 1, left - 1);
    ld f2 = f(cur + 1, left);
    ans1 = 2.0 * pi * v[cur].F * v[cur].S + f1;
    if (left == k) {
        ans1 += pi * v[cur].F * v[cur].F;
    }
    ans2 = f2;
    ld ans;
    if (f1 == -1 && f2 == -1) {
        ans = -1;
    } else if (f1 == -1) {
        ans = ans2;
    } else if (f2 == -1) {
        ans = ans1;
    } else {
        ans = max(ans1, ans2);
    }
    vis[cur][left] = 1;
    dp[cur][left] = ans;
    return ans;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int I = 1; I <= T; ++I) {
        v.clear();
        int r, h;
        cin >> n >> k;
        for (int i = 0; i < n + 5; ++i) {
            for (int j = 0; j < n + 5; ++j) {
                vis[i][j] = 0;
            }
        }
        for (int i = 0; i < n; ++i) {
            cin >> r >> h;
            v.push_back(mp(r, h));
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        cout << "Case #" << I << ": " << fixed << setprecision(10) << f(0, k) << endl;
    }

    return 0;
}

