#include<bits/stdc++.h>
using namespace std;
#define loop(i,L,R) for(int i=(L);i<=(R);i++)
#define rept(i,L,R) for(int i=(L);i<(R);i++)
#define isc(n) scanf("%d",&n)
#define llsc(n) scanf("%lld",&n)
#define dsc(n) scanf("%lf",&n)
#define enl cout<<endl
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define xx first
#define yy second
typedef long long ll;
typedef pair<int,int>PI;
typedef pair<pair<int,int>,int>PII;

pair<ll,ll> rec(ll n, ll k)
{
    if(k==1)
    {
        n--;
        return MP(n/2,n-n/2);
    }
    n--;
    k--;
    ll a=n/2, b=n-n/2;
    if(k%2==1)return rec(b,k-k/2);
    else return rec(a,k-k/2);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=0;
    isc(t);
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        pair<ll,ll> ans=rec(n,k);
        cout<<"Case #"<<++cas<<": "<<max(ans.xx,ans.yy)<<" "<<min(ans.yy,ans.xx)<<endl;
    }
    return 0;
}
