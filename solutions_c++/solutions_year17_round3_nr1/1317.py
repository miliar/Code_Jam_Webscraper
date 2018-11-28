#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define ld long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pld pair<ld,ld>
using namespace std;
struct pan
{
    ll r, h;
};
bool cmp(pan a, pan b)
{
    return a.r*a.h > b.r*b.h;
}
const int maxn = 1005;
int n, k;
pan pans[maxn];
ld pi = 3.14159265358979323846;
ld _main()
{
    ll ret = 0;
    cin >> n >> k;
    for(int i = 0; i < n; i++)
    {
        ll a, b; cin >> a >> b;
        pans[i] = {a,b};
    }
    for(int i = 0; i < n; i++)
    {
        vector <pan> v;
        ll tmp = 0;
        for(int j = 0; j < n; j++)if(pans[j].r <= pans[i].r && i != j)v.pb(pans[j]);
        sort(v.begin(), v.end(), cmp);
        if(v.size() < k-1)continue;
        for(int j = 0; j < k-1; j++)tmp += 2 * v[j].r * v[j].h;
        tmp += pans[i].r*pans[i].r + 2 * pans[i].r * pans[i].h;
        ret = max(ret, tmp);
    }
    return pi * ret;
}
int main()
{
    freopen("large.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt; cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        cout << "Case #" << i << ": " << fixed << setprecision(12) << _main() << "\n";
    }
    return 0;
}
