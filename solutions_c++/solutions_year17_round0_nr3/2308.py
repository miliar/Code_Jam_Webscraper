#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <cstring>

#define ll long long
#define f first
#define s second
#define INF (ll)(1e18 + 7)
#define EPS (1e-6)
#define pb push_back
#define mp make_pair

using namespace std;
ll n, k, v, t, ff, ss;
set <ll> s;
map <ll, ll> ma;
pair <ll, ll> ans;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    cin >> t;
    for (int ttt = 1; ttt <= t; ttt++)
    {
        s.clear();
        ma.clear();
        cin >> n >> k;

        std::set<ll>::iterator it;
        s.insert(n);
        ma[n]++;
        ans.f = ans.s = INF;

        while(!s.empty())
        {
            if (k <= 0)
                break;

            it = s.end();
            it--;
            v = *it;
            k -= ma[v];
            //cout << ma[v] << endl;
            v--;
            ff = v / 2;
            ss = v / 2 + v % 2;
            if (ff > 0)
                ma[ff] += ma[v + 1];
            if (ss > 0)
                ma[ss] += ma[v + 1];
            if (ff > 0)
                s.insert(ff);
            if (ss > 0)
                s.insert(ss);
            ans.f = min(ss, ans.f);
            ans.s = min(ff, ans.s);
           // cout << *it << ' ';
            s.erase(*it);
        }

        cout << "Case #" << ttt << ": " << ans.f << ' ' << ans.s << endl;
    }
/*
    for (it = s.end(); it != s.begin(); --it)
        cout << *it << ' ';
*/
    return 0;
}
