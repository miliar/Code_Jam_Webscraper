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
 
#define MAXN 100005

int main()
{
	int t,T;
	cin>>T;
	for(t = 1;t<=T;t++)
	{
		int n,r,o,y,g,b,v;
		int m;
		cin>>n>>r>>o>>y>>g>>b>>v;
		pair<int,char> a[3];
		
		a[0].fi = r;
		a[1].fi = y;
		a[2].fi = b;
		
		a[0].se = 'R';
		a[1].se = 'Y';
		a[2].se = 'B';
		
		char s[n+1];
		int k = 0;
		rep(i,n/2+1)
		{
			sort(a,a+3);
			s[k] = a[2].se;
			a[2].fi--;
			++k;
			if(a[1].fi > 0){
				s[k] = a[1].se;
				a[1].fi--;	
				++k;
			}
		}
		s[n] = '\0';
		bool flag = true;
		if(s[0]==s[n-1])
			flag = false;
		rep(i,n-1)
			if(s[i]==s[i+1])
			{
				flag = false;
				break;
			}
		if( flag == false )
		{
			flag = true;
			char c;
			c = s[n-1];
			s[n-1] = s[n-2];
			s[n-2] = c;
			if(s[0]==s[n-1])
				flag = false;
			rep(i,n-1)
				if(s[i]==s[i+1])
				{
					flag = false;
					break;
				}
				
		}
		if(flag)
			cout<<"Case #"<<t<<": "<<s<<el;
		else
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<el;
	}	
	return 0;
} 