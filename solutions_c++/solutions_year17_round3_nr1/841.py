#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
#define ff first
#define ss second
using namespace std;
typedef long long ll;
const int MOD = 0;
const int MAXN = 1005;
const double pi = acos(-1);

double r[MAXN];
double h[MAXN];
pair<double, int> side[MAXN];

double solve()
{
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> r[i] >> h[i];
        side[i].ff = h[i]*r[i]*2*pi;
        side[i].ss = i;
    }

    sort(side, side+n);

    double ans = 0;

    for (int i = 0; i < n; i++)
    {
        double res = pi * r[i] * r[i] + h[i]*r[i]*2*pi;
        int l = 1;
        for (int j = n-1; j >= 0 && l < k; j--)
        {
            if (side[j].ss == i || r[side[j].ss] > r[i]) continue;
            res += side[j].ff;
            l++;
        }
        if (l == k)
        {
            ans = max(ans, res);
        }
    }

    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout << setprecision(10) << fixed;
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cout << "Case #" << tt << ": " << solve() << endl;
    }

    return 0;
}


