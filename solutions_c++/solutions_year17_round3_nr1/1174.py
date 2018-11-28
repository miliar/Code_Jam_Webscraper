#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define vi vector<int>
#define vl vector<ll>
#define vii vector<pii >
#define vll vector<pll>
#define pll pair<ll,ll>
#define pii pair<int,int>

#define EL printf("\n")
#define OK printf("OK");
#define foreach(i,t) for(auto i =t.begin();i!=t.end();i++) 
#define pii pair<int,int>
#define pdn(n) printf("%d\n",n)
#define psn(n) printf("%s\n",n)
#define pcn(n) printf("%c\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define ss(n) scanf("%s",&n)
#define pn printf("\n")
#define  omap unordered_map
#define SZ(x) ((int)(x.size()))
#define foi(i,a,n) for(int (i)=int(a);(i)<=int(n);++(i))
#define fod(i,a,n) for(int (i)=int(a);(i)>=int(n);--(i))

#define inf 1e16
#define mod 1000000007
#define precise(n,k) fixed<<setprecision(k)<<n
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)
#define fequal(a,b) (fabs(a - b)<(1e-9))
int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
typedef long long ll;
typedef long double lf;
#define pi lf(3.14159265)
ll pw(ll a,ll b) 
{if(b==0) return 1; if(b==1) return a;  ll ans=pw(a,b/2); if(b&1) 
return (((ans*ans)%mod*a)%mod); 
 return (ans*ans)%mod; }	
ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO"<<endl;else cout<<"YES"<<endl;exit(0);}

pair<lf,lf> disk[1200];

lf dp[1200][1200];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int tt;
	cin>>tt;

	for(int tc=1;tc<=tt;tc++)
	{
		
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++)
			cin>>disk[i].fi>>disk[i].se;

		sort(disk+1,disk+n+1);
		
		for(int i=0;i<=n;i++)
			for(int j=0;j<=k;j++)
				dp[i][j]=-inf;

		for(int i=0;i<=n;i++)
			dp[i][0]=0;
	
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=k-1;j++)
			{
				dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*pi*disk[i].fi*disk[i].se);
			}
		}

		lf ans=0;
		for(int i=1;i<=n;i++)
		{
			ans=max(ans,dp[i-1][k-1]+2*pi*disk[i].fi*disk[i].se+pi*disk[i].fi*disk[i].fi);
		}
	
		cout<<"Case #"<<tc<<": "<<precise(ans,10)<<endl;

	}
	//cout<<RTIME<<endl;
	return 0;
}