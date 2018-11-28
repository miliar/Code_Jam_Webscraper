#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, p;
    cin >> n >> p;
    vector<int> a(p, 0);
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        a[x % p]++;
    }

    int ans = 0;
    ans += a[0];
    switch (p)
    {
        case 2:
            ans += (a[1] + 1) / 2;
            break;

        case 3:
            if (a[1] == a[2])
                ans += a[1];
            else if (a[1] < a[2])
                ans += a[1] + (a[2] - a[1] + 2) / 3;
            else
                ans += a[2] + (a[1] - a[2] + 2) / 3;
            break;

        case 4:
            ans += a[2] / 2;
            a[2] %= 2;
            if (a[1] == a[3])
            {
                ans += a[1];
                if (a[2]) ans++;
            }
            else if (a[1] < a[3])
            {
                ans += a[1];
                a[3] -= a[1];
                ans += (a[3] + 2) / 3;
            }
            else
            {
                ans += a[3];
                a[1] -= a[3];
                ans += (a[1] + 2) / 3;
            }
            break;
    }
    cout << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
