#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
pll cnt[2];
pll split(ll x)
{
    if(x == 0 || x == 1)return {0, 0};
    else if(x % 2 == 1)return {x/2, x/2};
    else return {x/2, x/2-1};
}
ll mx(pll x)
{
    return max(x.f, x.s);
}
ll mn(pll x)
{
    if(x.f == 0)return x.s;
    if(x.s == 0)return x.f;
    return min(x.f, x.s);
}
pll _main()
{
    ll a, b;
    cin >> a >> b;
    cnt[0] = {a, 1};
    cnt[1] = {0, 0};
    while(1)
    {
        if(cnt[0].f == 1)return {0, 0};
        else if(cnt[0].f == 2)
        {
            if(cnt[0].s >= b)return {1, 0};
            else
            {
                cnt[0] = {1, cnt[0].s + cnt[1].s};
                cnt[1] = {0, 0};
            }
        }
        else
        {
            pll tmp1, tmp2;
            if(cnt[0].s >= b)return split(cnt[0].f);
            else
            {
                tmp1 = split(cnt[0].f);
                b -= cnt[0].s;
            }
            if(cnt[1].s >= b)return split(cnt[1].f);
            else
            {
                tmp2 = split(cnt[1].f);
                b -= cnt[1].s;
            }
            ll maxi = max(mx(tmp1), mx(tmp2)), mini = mn({mn(tmp1), mn(tmp2)}), sz1 = cnt[0].s, sz2 = cnt[1].s;
            cnt[0] = cnt[1] = {0, 0};
            cnt[0].f = maxi;
            cnt[1].f = mini;
            if(tmp1.f == maxi)cnt[0].s += sz1;
            else cnt[1].s += sz1;
            if(tmp1.s == maxi)cnt[0].s += sz1;
            else cnt[1].s += sz1;
            if(tmp2.f == maxi)cnt[0].s += sz2;
            else cnt[1].s += sz2;
            if(tmp2.s == maxi)cnt[0].s += sz2;
            else cnt[1].s += sz2;
            if(cnt[1].f == 0)cnt[1].s = 0;
        }
    }
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        pll ret = _main();
        cout << "Case #" << i << ": " << ret.f << " " << ret.s << " \n";
    }
    return 0;
}
