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

ll r,c;
vvc v;

void func(ll r1,ll c1,char ch)
{
	for(ll j=c1+1;j<c;j++)
	{
		if(v[r1][j]=='?')
		{
			v[r1][j]=ch;
		}
		else
		{
			break;
		}
	}
	for(ll j=c1-1;j>=0;j--)
	{
		if(v[r1][j]=='?')
		{
			v[r1][j]=ch;
		}
		else
		{
			break;
		}
	}
}

void func2(ll r1,ll c1,char ch)
{
	for(ll j=r1+1;j<r;j++)
	{
		if(v[j][c1]=='?')
		{
			v[j][c1]=ch;
		}
		else
		{
			break;
		}
	}
	for(ll j=r1-1;j>=0;j--)
	{
		if(v[j][c1]=='?')
		{
			v[j][c1]=ch;
		}
		else
		{
			break;
		}
	}
}
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("A-large (2).in", "r" , stdin);
	freopen("output.txt", "w", stdout);
	#endif 
	ll t;
	cin>>t;
	ll z=0;
	while(z++<t)
	{
		cin>>r>>c;
		v=vvc (r,vc(c));
		bool checkrow=false;
		for(ll i=0;i<r;i++)
		{
			bool check=true;
			for(ll j=0;j<c;j++)
			{
				cin>>v[i][j];
				if(v[i][j]!='?')
				{
					check=false;
				}
			}
			if(check)
			{
				checkrow=true;
			}
		}
		vvc v2=v;
		bool check1=true;
		ll ct=0;
		while(check1)
		{
			ct++;
			check1=false;
			for(ll i=0;i<r;i++)
			{
				for(ll j=0;j<c;j++)
				{
					if(v2[i][j]!='?')
					{
						if(ct<10)
							func(i,j,v[i][j]);
						else
							func2(i,j,v[i][j]);
					}
				}
			}
			for(ll i=0;i<r;i++)
			{
				for(ll j=0;j<c;j++)
				{
					if(v[i][j]=='?')
					{
						check1=true;
						break;
					}
				}
			}
			v2=v;
		}
		cout<<"Case #"<<z<<":"<<endl;
		for(ll i=0;i<r;i++)
		{
			for(ll j=0;j<c;j++)
			{
				cout<<v[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
