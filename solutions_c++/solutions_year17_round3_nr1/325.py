#include <bits/stdc++.h>

using namespace std;

struct pancake
{
    long long r, h;
    bool operator<(const pancake& p) const
    {
        if (r == p.r)
            return h > p.h;
        else
            return r > p.r;
    }
} a[1010];

void solve()
{
    int n, k;

    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> a[i].r >> a[i].h;
    sort(a, a + n);
    vector<long long> v;
    long long ans = 0;
    for (int i = 0; i < n; i++)
    {
        v.clear();
        for (int j = i + 1; j < n; j++)
            v.push_back(a[j].h * a[j].r);
        if (v.size() < k - 1) break;
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        long long sum = 0;
        for (int j = 0; j < k - 1; j++)
            sum += v[j];
        ans = max(ans,
                2ll * a[i].r * a[i].h
                + a[i].r * a[i].r + 2ll * sum);
    }
    cout << setprecision(20) << M_PI * ans << endl;
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
