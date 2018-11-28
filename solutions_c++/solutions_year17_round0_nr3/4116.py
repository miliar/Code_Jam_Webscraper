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
struct cmp
{
    bool operator()(pii x,pii y)
    {
        if(((x.fi-1)/2)==((y.fi-1)/2))
        {
            if((x.fi/2)==(y.fi/2)) return x.se<y.se;
            else return x.fi<y.fi;
        }
        else return x.fi<y.fi;
    }
};
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    /*priority_queue<ll> q;
    ll n,k=0;
    cin>>n;
    q.push(n);
    while(true)
    {
        k++;
        ll z=q.top();
        q.pop();
        cout<<k<<": "<<(z-1)/2<<" "<<z/2<<endl;
        q.push((z-1)/2);
        q.push(z/2);
        char c=getchar();
    }*/
    ll t,T;
    cin>>t;
    T=t;
    while(t--)
    {
        ll n,k,z1,z2;
        cin>>n>>k;
        priority_queue<pii,vector<pii >,cmp> q;
        q.push(mp(n,0));
        while(k--)
        {
            pii z=q.top();
            q.pop();
            z1=(z.fi-1)/2;
            z2=z.fi/2;
            q.push(mp(z1,z.se));
            q.push(mp(z2,z.se+((z.se+1)/2)));
        }
        cout<<"Case #"<<T-t<<": "<<z2<<" "<<z1<<endl;
    }
    return 0;
}

