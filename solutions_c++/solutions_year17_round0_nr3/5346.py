#include <bits/stdc++.h>

using namespace std;
#define ll long long
int main()
{
    freopen("C-small-2-attempt0.in","rt",stdin);
    freopen("C-small-2-attempt0.out","wt",stdout);
    ll t;
    cin >> t;
    for(ll w = 1;w <= t;w++)
    {
        ll n,k;
        cin >> n >> k;
        pair<ll,ll> ps = make_pair(1,n);
        ll x = (ps.second-ps.first)/2+(ps.second-ps.first)%2+ps.first;
        ll ls = x-ps.first;
        ll rs = ps.second-x;
        pair<ll,ll> pf = make_pair(min(ls,rs),max(ls,rs));
        priority_queue <pair<pair<ll ,ll> , pair<ll ,ll> > > que;
        //min max start end
        que.push(make_pair(pf,ps));
        for(ll i = 0;i < k-1;i++)
        {
            pair<pair<ll ,ll> , pair<ll ,ll> > pall = que.top();
            que.pop();
            ps = pall.second;
            x = (ps.second-ps.first)/2+(ps.second-ps.first)%2+ps.first;
            pair<ll,ll> psy = make_pair(ps.first,x-1);
            ll y = (psy.second-psy.first)/2+(psy.second-psy.first)%2+psy.first;
            ls = y-psy.first;
            rs = psy.second-y;
            pf = make_pair(min(ls,rs),max(ls,rs));
            que.push(make_pair(pf,psy));
            //
            psy = make_pair(x+1,ps.second);
            y = (psy.second-psy.first)/2+(psy.second-psy.first)%2+psy.first;
            ls = y-psy.first;
            rs = psy.second-y;
            pf = make_pair(min(ls,rs),max(ls,rs));
            que.push(make_pair(pf,psy));
        }
        pair<pair<ll ,ll> , pair<ll ,ll> > pall = que.top();
        que.pop();
        pf = pall.first;
        cout << "Case #"<<w<<": " << pf.second << " " << pf.first << endl;
    }
    return 0;
}
