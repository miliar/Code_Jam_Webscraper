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
#define pi 3.14159265358979
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
#define PI 3.14159265
#define inf 1e18
#define mod 1000000007
#define precise(n,k) fixed<<setprecision(k)<<n
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)
#define fequal(a,b) (fabs(a - b)<(1e-9))
int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
typedef long long ll;
typedef long double lf;

ll pw(ll a,ll b) 
{if(b==0) return 1; if(b==1) return a;  ll ans=pw(a,b/2); if(b&1) 
return (((ans*ans)%mod*a)%mod); 
 return (ans*ans)%mod; }	
ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO"<<endl;else cout<<"YES"<<endl;exit(0);}


lf arr[100];
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		int n,k;
		cin>>n>>k;
		lf u;
		cin>>u;
		for(int i=1;i<=n;i++)
			cin>>arr[i];
		arr[n+1]=1;
		sort(arr+1,arr+n+1);
		for(int i=1;i<=n&&u;i++)
		{
			lf diff=arr[i+1]-arr[i];
			//cout<<diff<<endl;
			lf each=min(diff,u/i);
			// cout<<"Each "<<each<<endl;
			for(int j=1;j<=i;j++)
				arr[j]+=each;
			// for(int j=1;j<=n;j++)
			// 	cout<<arr[j]<<"-->";
			//cout<<endl;
			u-=each*i;

		}
		lf ans=1;
		for(int i=1;i<=n;i++)
			{
				//cout<<arr[i]<<endl;
				ans*=arr[i];
			}
		cout<<"Case #"<<p<<": "<<precise(ans,10)<<endl;
	}
	return 0;
}