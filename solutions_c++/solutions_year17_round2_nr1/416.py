#include <bits/stdc++.h>

using namespace std;

const int MaxN = 1e3 + 15;
const int INF = 1e9;
const int MOD = 1e9 + 7;

int cases;

long double d;
int n;

pair<long double, long double> a[MaxN];

void solve()
{
    ++cases;
    cout << "CASE #" << cases << ": ";
    cin >> d >> n;

    long double mn = 0;

    for(int i = 1; i <= n; ++i)
    {
        cin >> a[i].first >> a[i].second;
    }

    sort(a + 1, a + n + 1);

    for(int i = n; i; --i)
    {
        long double cur = (d - a[i].first) / a[i].second;
        if(cur < mn)
            cur = mn;
        else
            mn = cur;
    }

    cout.precision(9);
    cout << fixed << d / mn << '\n';
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t --> 0)
        solve();
    return 0;
}
