#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
using namespace std;
typedef long long ll;
const int MOD = 0;
const int MAXN = 100005;


double pref[MAXN];
double p[MAXN];
double solve()
{
    int n, k;
    double u;
    cin >> n >> k;
    cin >> u;

    for (int i = 1; i <= n; i++)
        cin >> p[i];
    sort(p+1, p + n+1);

    pref[0] = 0;
    for (int i = 1; i <= n; i++)
        pref[i] = pref[i-1] + p[i];

    int i = 1;
    while (i < n && (u + pref[i])/(double)(i) > p[i+1]) i++;
    double x = (u + pref[i])/(double)(i);

    //DEBUG(i);
    //DEBUG(x);

    double ans = 1;
    for (int j = 1; j <= i; j++)
        ans *= x;
    for (int j = i+1; j <= n; j++)
        ans *= p[j];

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


