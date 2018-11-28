#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vii;
typedef vector<vector<int> > vvi;
typedef vector<vector<long long> > vvii;
typedef vector< pair<ll,ll> > vpii;
 
#define boost std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define FOR(i,a,b) for(i= (a) ; i<(b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).rbegin() , (x).rend()
#define out(x) cout<<x<<"\n"
#define nl cout<<"\n"
#define INF 1000001
#define F first
#define S second
#define pi 3.14159265358979323846
 
typedef struct node
{
	ll r,h,idx;
}node;
int main()
{
    boost;
    int t,tc=1;
    cin>>t;
    while(t--)
    {
        ll n,m,i,j,k,x,y,z;
        cin>>n>>k;
        node a[n];
        FOR(i,0,n) cin>>a[i].r>>a[i].h;
        FOR(i,0,n) a[i].idx=i;
        vpii b(n);
        FOR(i,0,n)
        {
        	b[i].F = a[i].r*a[i].h;
        	b[i].S = i;
        }
        sort(all(b));
        double ans=0.0;
        FOR(i,0,n)
        {
        	double tmp = 2*pi*a[i].r*a[i].h + pi*a[i].r*a[i].r;
        	int cnt=1;
        	FOR(j,0,n)
        	{
        		if(cnt==k) break;
        		if(b[j].S==i) continue;
        		double lol = 2*pi*b[j].F;
        		tmp+=lol;
        		cnt++;
        	}
        	ans=max(ans,tmp);
        }
        printf("Case #%d: %.8f\n",tc,ans); 
        tc++;
        // cout<<"Case #"<<tc++<<": "<<setprecision()<<ans; nl;
    }
    return 0;
}     