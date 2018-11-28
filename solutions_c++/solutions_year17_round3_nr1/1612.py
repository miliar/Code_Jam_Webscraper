#include<bits/stdc++.h>
#define rep(i,start,lim) for(lld i=start;i<lim;i++)
#define repd(i,start,lim) for(lld i=start;i>=lim;i--)
#define scan(x) scanf("%lld",&x)
#define print(x) printf("%lld ",x)
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define br printf("\n")
#define YES printf("YES\n")
#define NO printf("NO\n")
#define all(c) (c).begin(),(c).end()
using namespace std;
#define INF         1011111111
#define LLINF       1000111000111000111LL
#define EPS         (double)1e-10
#define MOD         1000000007
#define PI          3.14159265358979323
using namespace std;
typedef long double ldb;
typedef long long lld;
lld powm(lld base,lld exp,lld mod=MOD) {lld ans=1;while(exp){if(exp&1) ans=(ans*base)%mod;exp>>=1,base=(base*base)%mod;}return ans;}
typedef vector<lld> vlld;
typedef pair<lld,lld> plld;
typedef map<lld,lld> mlld;
typedef set<lld> slld;
#define N 1005
vector<lld> v;
lld r[N],h[N];
int main()
{
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	lld t,n,k,x,y;
	ldb ans,maxm=0;
	cin>>t;
	rep(tt,1,t+1)
	{
		cin>>n>>k,maxm=0;
		v.clear();
		rep(i,1,n+1) cin>>r[i]>>h[i];
		rep(base,1,n+1) 
		{
			ans=PI*r[base]*r[base];
			v.clear();
			v.pb(r[base]*h[base]);
			rep(i,1,n+1) if(i!=base and r[i]<=r[base]) v.pb(r[i]*h[i]);
			sort(v.begin()+1,v.end()),reverse(v.begin()+1,v.end());
			//cout<<base<<endl;
			//for(auto i:v) cout<<i<<" ";br;
			if(v.size()>=k) {
				rep(i,0,k) ans+=2*PI*v[i];
				maxm=max(maxm,ans); 
			}
			//cout<<base<<" "<<maxm<<endl;
		}	
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(7)<<maxm<<endl;
	}
	return 0;
}