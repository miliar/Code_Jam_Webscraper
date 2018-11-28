#include<bits/stdc++.h>
using namespace std;
#define ll                  long long
#define ld                  long double
#define rep(i,n)            for(ll i=0;i<n;i++)
#define hell                1000000007LL
#define vi                  vector<ll>
#define vii                 vector< vi >
#define pb                  push_back
#define mp                  make_pair
#define fi                  first
#define se                  second
#define pii                 pair<ll,ll>
#define all(c)              c.begin(),c.end()
#define sz(c)               c.size()
ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }
ll power(ll x, ll y,ll p)
{
    ll res=1;
    x=x%p;
    while(y>0)
    {
        if(y&1)
            res=((res%p)*(x%p))%p;
        y=y>>1;
        x=((x%p)*(x%p))%p;
    }
    return res;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t,T;
    cin>>t;
    T=t;
    while(t--)
    {
        ll N,m;
        cin>>N;
        m=N;
        string n,ans;
        while(N>0)
        {
            n.pb((N%10)+'0');
            N/=10;
        }
        reverse(all(n));
        N=m;
        for(ll i=0;i<sz(n);i++)
        {
            ll in=0;
            ll p=0;
            if(i!=0) p=(ans[sz(ans)-1]-'0');
            for(ll j=9;j>=p;j--)
            {
                string z=ans;
                rep(k,sz(n)-i) z.pb((j+'0'));
                if(z<=n)
                {
                    in=j;
                    break;
                }
            }
            ans.pb((in+'0'));
        }
        reverse(all(ans));
        while(ans.empty()!=true && ans[sz(ans)-1]=='0') ans.pop_back();
        reverse(all(ans));
        cout<<"Case #"<<T-t<<": "<<ans<<endl;
    }
    return 0;
}

