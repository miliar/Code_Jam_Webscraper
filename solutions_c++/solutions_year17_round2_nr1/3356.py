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
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
#define  omap unordered_map
#define PI 3.14159265
#define Inf 1e9
#define mod 1000000007
#define precise(n,k) fixed<<setprecision(k)<<n
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)
#define fequal(a,b) (fabs(a - b)<(1e-9))
int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
typedef long long ll;
typedef long double lf;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO"<<endl;else cout<<"YES"<<endl;exit(0);}


int main()
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		ll d,n;
		cin>>d>>n;
		lf ans=1e14;
		for(int i=1;i<=n;i++)
		{
			lf h,s;
			cin>>h>>s;
			ans=min(ans,(d*s)/(d-h));
		}
		cout<<"Case #"<<p<<": "<<precise(ans,8)<<endl;
	}
	return 0;	
}