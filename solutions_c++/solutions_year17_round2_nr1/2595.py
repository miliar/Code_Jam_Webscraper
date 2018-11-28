#include <bits/stdc++.h>

#define dout2(x) cout << #x << " = "<< (x) << "\n";

using namespace std;

typedef long long ll;
typedef long double ld;

void print(int test, ld ans)
{
    cout << setprecision(9) << fixed << "Case #" << test << ": " << ans << "\n";
}

void solve(int test)
{
    ld d;
    int n;
    cin >> d >> n;

    ld ans = 0;
    for (int i = 0; i < n; i++)
    {
        ld p, s;
        cin >> p >> s; 
        ans = max(ans, (d - p) / s);       
    }
    print(test, d / ans);
}

signed main()
{
#ifdef PC
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    int t = 0;
    cin >> t;
    for (int i = 1; i <= t; i++)
        solve(i);
    return 0;
}