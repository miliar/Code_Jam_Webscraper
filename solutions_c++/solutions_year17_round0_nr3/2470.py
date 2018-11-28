#include <bits/stdc++.h>
using namespace std;
typedef double ld;
#define y1 cgbngfgn
#define pb push_back
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define fir first
#define m_p make_pair
#define sec second
typedef long long ll;
#define files(name) freopen(name".sol","r",stdin); freopen (name".dat","w",stdout);
pair<ll,ll> get()
{
    multiset<pair<ll,ll> > mp;
    map<ll,ll> cnt;
    ll n,k;
    cin>>n>>k;
    cnt[n]=1;
    mp.insert({n,1});
    while (k)
    {
        pair<ll,ll> now=*mp.rbegin();
        if (now.sec>=k)
        {
            return(m_p((now.fir-ll(1))/ll(2),now.fir/ll(2)));
        }
        k-=now.sec;
        mp.erase(now);
        cnt[now.fir]=0;

        mp.erase({(now.fir-1)/2,cnt[(now.fir-1)/2]});
        mp.erase({(now.fir)/2,cnt[(now.fir)/2]});
        cnt[(now.fir-1)/2]+=now.sec;
        cnt[(now.fir)/2]+=now.sec;
        mp.insert({(now.fir-1)/2,cnt[(now.fir-1)/2]});
        if (now.fir%2==0)
        {
            mp.insert({(now.fir)/2,cnt[(now.fir)/2]});
        }
    }
}
signed main()
{
    //files("graph");
    ll t ;
    cin>>t;
    for (ll i=1;i<=t;i++)
    {
        pair<ll,ll> now=get();
        cout<<"case #"<<i<<": "<<now.sec<<' '<<now.fir<<'\n';
    }
}
/*1000000000000000000 1000000000000000000*/
