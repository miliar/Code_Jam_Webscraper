#include<bits/stdc++.h>
#include <ext/numeric>
using namespace std;
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define scd(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf%lf",&a,&b)
#define scd3(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)
#define scd4(a,b,c,d) scanf("%lf%lf%lf%lf",&a,&b,&c,&d)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ALL(x) x.begin(), x.end()
#define BUFF ios::sync_with_stdio(false);
#define endl "\n"
#define power(a,x) __gnu_cxx::power(a, x)
#define forN(i,n) for(int i=0;i<n;i++)
#define eps 1e-5
#define INF INT_MAX
#define INFLL LLONG_MAX
#define gcd(a,b) __gcd(a,b)
typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vector<int> >vvi;
#define cin in
#define cout out
map<ll,ll> dp;
map<ll,bool> vis;

ll solve(ll n,ll k)
{
    priority_queue<ll> pq;
    pq.push(n);
    dp[-n]=1;
    while(!pq.empty())
    {
        ll curr=pq.top();
        pq.pop();
        if(vis[curr]|| curr<=1)continue;
        vis[curr]=true;
        ll m1=curr/2;
        ll m2=curr-m1;
        ll mx=max(m1,m2);
        ll mn=min(m1,m2);
        mx-=1;
        dp[-mx]+=dp[-curr];
        dp[-mn]+=dp[-curr];
        if(!vis[mx])pq.push(mx);
        if(!vis[mn])pq.push(mn);
    }
    ll r=0;
    for(map<ll,ll>::iterator it=dp.begin();it!=dp.end();it++)
    {
        r+=it->se;
        //cout<<r<<endl;
        if(r>=k)return -it->fi;
    }
    return 1;
}
int main()
{
    ifstream in;
    ofstream out;
    in.open ("in.in");
    out.open ("out.txt");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        dp.clear();
        vis.clear();
        ll n,k;
        cin>>n>>k;
        ll curr=solve(n,k);
        ll m1=curr/2;
        ll m2=curr-m1;
        ll mx=max(m1,m2);
        ll mn=min(m1,m2);
        mx-=1;
        cout<<"Case #"<<tt<<": "<<max(mx,mn)<<" "<<min(mn,mx)<<endl;
    }
    in.close();
    out.close();
    return 0;
}
