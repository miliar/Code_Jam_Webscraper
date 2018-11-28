#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define Max(x,y,z) max(x,max(y,z))
#define Min(x,y,z) min(x,min(y,z))
#define fr(i,s,e) for(i=s;i<e;i++)
#define rf(i,s,e) for(i=s-1;i>=e;i--)
#define pb push_back
#define eb emblace_back
#define mp make_pair
#define ff first
#define ss second
#define trace1(x)                cerr<<#x<<": "<<x<<endl
#define trace2(x, y)             cerr<<#x<<": "<<x<<" | "<<#y<<": "<<y<<endl
#define trace3(x, y, z)          cerr<<#x<<":" <<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl
#define trace4(a, b, c, d)       cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl
#define trace5(a, b, c, d, e)    cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<endl
#define trace6(a, b, c, d, e, f) cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<" | "<<#f<<": "<<f<<endl

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;
typedef vector<long long> vll;
typedef vector<vll> vvll;
typedef vector<vvll> vvvll;
typedef vector<vvvll> vvvvll;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<vvc> vvvc;
typedef vector<pair<long long,long long> > vpll;
typedef vector<vector<pair<ll,ll> > > vvpll;
typedef vector<bool> vb;
typedef vector<vb> vvb;

#define PI 3.141592653589793
#define MOD 1000000007

template<typename T> T gcd(T a,T b) { if(a==0) return b; return gcd(b%a,a); }
template<typename T> T pow(T a,T b, ll m){T ans=1; while(b>0){ if(b%2==1) ans=(ans*a)%m; b/=2; a=(a*a)%m; } return ans%m; }

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("A-large (4).in", "r" , stdin);
	freopen("output.txt", "w", stdout);
	#endif
	ll t;
	cin>>t;
	ll z=0;
	while(z++<t)
	{
		ll n,k;
		cin>>n>>k;
		vector<long double> r(n),h(n);
		vector<pair<long double,long double>> v(n);
		vector<pair<long double,long double>> v2(n);
		for(ll i=0;i<n;i++)
		{
			cin>>r[i]>>h[i];
			v[i].ff=r[i]*h[i];
			v[i].ss=r[i];
			v2[i].ff=r[i];
			v2[i].ss=h[i];
		}
		sort(v.rbegin(),v.rend());
		sort(v2.rbegin(),v2.rend());
		long double ans=0;
		for(ll i=0;i<=n-k;i++)
		{
			long double topar=PI*v2[i].ff*v2[i].ff;
			long double str=v2[i].ff;
			ll ct=1;
			bool check=false;
			long double sidear=2*PI*v2[i].ff*v2[i].ss;
			for(ll j=0;j<n;j++)
			{
				if(v[j].ss>str)
				{
					continue;
				}
				if(!check&&v[j].ss==str&&v[j].ff/v[j].ss == v2[i].ss)
				{
					check=true;
					continue;
				}
				if(ct>=k)
				{
					break;
				}
				ct++;
				sidear+=v[j].ff*2*PI;
			}
			long double tempans=topar+sidear;
			ans=max(ans,tempans);
		}
		cout<<"Case #"<<z<<": "<<fixed<<setprecision(10)<<ans<<endl;
	}
	return 0;
}
