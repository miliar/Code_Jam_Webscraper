#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector <pair <pair <ll, ll>, ll> > e;
map <ll, ll> kek;
set <ll> vis;
vector <ll> all;

void prec(ll n)
{
    if (!n)
    {
        return;
    }
    if (vis.count(n))
    {
        return;
    }
    all.push_back(n);
    vis.insert(n);
    ll l1, l2;
    if (n % 2 == 1)
    {
        l1 = n / 2, l2 = n / 2;
    }
    else
    {
        l1 = n / 2, l2 = max(0ll, n / 2 - 1);
    }
    prec(l1), prec(l2);
}

void bfs(ll n)
{
    prec(n);
    sort(all.begin(), all.end());
    for (int i = (int) all.size() - 1; i >= 0; i--)
    {
        ll n = all[i];
        ll l1, l2;
        if (n % 2 == 1)
        {
            l1 = n / 2, l2 = n / 2;
        }
        else
        {
            l1 = n / 2, l2 = max(0ll, n / 2 - 1);
        }
        kek[l1] += kek[n];
        kek[l2] += kek[n];
        e.push_back({{l1, l2}, n});
    }
}

int main()
{
#ifdef ONPC
    freopen("lurege.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int it = 0; it < t; it++)
    {
        ll n, k;
        cin >> n >> k;
        kek.clear();
        vis.clear();
        all.clear();
        e.clear();
        kek[n] = 1;
        bfs(n);
        sort(e.rbegin(), e.rend());
        ll st = k;
        for (auto c : e)
        {
            if (kek[c.second] >= k || c.second == 0)
            {
                cout << "Case #" << it + 1 << ": " << c.first.first << ' ' << c.first.second << '\n';
                break;
            }
            else
            {
                k -= kek[c.second];
            }
        }
    }
}
