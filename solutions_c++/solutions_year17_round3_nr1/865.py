#include <bits/stdc++.h>
using namespace std;

#define in cin
#define out cout

#define REP(i,n) for(int i=0; i<n; i++)
#define REP2(i,s,e) for(int i=s; i<e; i++)
#define REPD(i,s,e,d) for(int i=s; i<=e; i+=d)
#define REPE(i,s,e) for(int i=s; i<=e; i++)
#define REPR(i,s,e) for(int i=s; i>=e; i--)

#define all(v) v.begin(), v.end()
#define pb push_back

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define rd(n) scanf("%d", &n)

#define x first
#define y second
#define intINF 2147483647
#define llINF 9223372036854775807LL
#define MOD 1000000007

void solve(int tc)
{
    int n, k; cin >> n >> k;
    vector<pll> v(n);
    for(int i=0; i<n; i++)
    {
        cin >> v[i].x >> v[i].y;
    }

    ll res = 0;
    for(int i=0; i<n; i++)
    {
        ll sum = v[i].x * v[i].x + 2LL*v[i].x*v[i].y;

        vector<pii> t;
        vector<ll> surf;
        for(int j=0; j<n; j++)
        {
            if(i == j) continue;
            if(v[i].x >= v[j].x) t.push_back(v[j]);
        }

        if(t.size() < k-1) continue;
        for(pii it : t)
        {
            surf.push_back(2LL*it.x * it.y);
        }
        sort(all(surf));
        reverse(all(surf));

        for(int i=0; i<k-1; i++)
        {
            sum += surf[i];
        }

        res = max(res, sum);
    }


    printf("Case #%d: %.9f\n", tc, res * acos(-1));
}

int main()
{
#ifndef ONLINE_JUDGE
     freopen("in.txt", "r", stdin);
     freopen("out.txt", "w", stdout);
#endif

    int tc; scanf("%d", &tc);
    for(int i=1; i<=tc; i++) solve(i);


    return 0;
}
