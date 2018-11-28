#include <iostream>
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const int maxn = 11000;

struct Pancake
{
    ll r;
    ll h;
    int i;
};

ll genAns = -1;

void get(int n, int k, int cnt, int last, ll res, Pancake b[])
{
    if (cnt == k)
    {
        genAns = max(genAns, res);
        return;
    }
    for (int i = last + 1; i < n; i++)
    {
        get(n, k, cnt + 1, i, res + 2 * b[i].h * b[i].r, b);
    }
}

ll get(int n, int k, Pancake b[])
{
    genAns = -1;
    sort(b, b + n, [](Pancake p1, Pancake p2) -> bool {return p1.r > p2.r;});
    for (int i = 0; i < n - k + 1; i++)
    {
        get(n, k, 1, i, b[i].r * b[i].r + 2 * b[i].h * b[i].r, b);
    }
    return genAns;
}

int main(int argc, char *argv[])
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cout << "Case #" << tt << ": ";
        int n, k;
        cin >> n >> k;
        Pancake a[maxn] = {}, b[maxn] = {};
        for (int i = 0; i < n; i++)
        {
            cin >> a[i].r >> a[i].h;
            a[i].i = i;
            b[i] = a[i];
        }
        sort(a, a + n, [](Pancake p1, Pancake p2) -> bool {return p1.r * p1.h > p2.r * p2.h;});
        ll ans = 0;
        for (int i = 0; i < n; i++)
        {
            const Pancake &first = a[i];
            ll res = (first.r * first.r + (ll) 2 * first.h * first.r);
            int c = 1;
            for (int j = 0; j < n && c < k; j++)
            {
                if (j == i && a[j].r <= first.r)
                    continue;
                res += (ll) 2 * (a[j].h * a[j].r);
                c++;
            }
            if (c == k)
                ans = max(ans, res);
        }
        //cout << ans << '\n';
        //ll ans1 = get(n, k, b);
        //assert(ans == ans1);
        //cout << '\n';
        //cout << setprecision(40) << (long double) M_PI * ans1 << '\n';
        cout << setprecision(40) << (long double) M_PI * ans << '\n';
    }
    return 0;
}
