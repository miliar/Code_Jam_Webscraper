#include <bits/stdc++.h>
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define mp make_pair
#define pb push_back 
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sortv(a) sort(a.begin(),a.end())
#define test()  int t; cin>>t; while(t--)
#define fi first
#define se second
#define el "\n"
#define ll long long
#define ull unsigned ll
#define TRACE
using namespace std;
 
FILE *fin = freopen("input.txt","r",stdin);
FILE *fout = freopen("output.txt","w",stdout);
 
#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
 
#else
 
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
 
#endif
 
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;
 
#define MAXN 1000005

PII a[MAXN];

void solve()
{
	for(int i = 1;i<MAXN;i++)
	{
		a[i]=(mp(i/2,(i-1)/2));
	}
}
int main()
{
	int t,T;
	cin>>T;
	solve();
	for(t = 1;t<=T;t++)
	{
		ll n,k,f,s;
		cin>>n>>k;
		vector<int> v;
		int temp;
		PII ans;
		v.pb(n);
		while(!v.empty() && k--)
		{
			sort(all(v));
			temp = v[sz(v)-1];
			ans = a[temp];
			v.pop_back();
			f = a[temp].fi;
			s = a[temp].se;
			v.pb(f);
			v.pb(s);
		}
		if(k>0)
		{
			ans.fi = 0;
			ans.se = 0;
		}
		cout<<"Case #"<<t<<": "<<ans.fi<<" "<<ans.se<<el;
		while(!v.empty())
			v.pop_back();
	}	
	return 0;
} 