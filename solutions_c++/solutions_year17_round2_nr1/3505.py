#include <bits/stdc++.h>
using namespace std;

using ld = long double;

void solve(int t)
{
    int d, n; cin >> d >> n;

    ld max_time = 0;

    for(int i = 0; i < n; i++)
    {
        int k, s; cin >> k >> s;

        ld tm = ld(d - k) / ld(s);

        max_time = max(max_time, tm);
    }

    ld ans = ld(d) / ld(max_time);

    cout << "Case #" << t << ": " << setprecision(9) << fixed << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);

    int t; cin >> t;

    for(int i = 1; i <= t; i++) solve(i);

    return 0;
}
