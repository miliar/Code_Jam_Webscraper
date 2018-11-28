#include <bits/stdc++.h>
using namespace std;
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define forr(a,b,c) for(int a=b;a<c;a++)
#define forrev(a,b,c) for(int a=b;a>c;a--)
#define all(v) v.begin(),v.end()
#define revall(v) v.rbegin(),v.rend()
#define ff first
#define ss second
#define next ksfhuksfkhdn
#define prev uegrfjsfgsji
#define count jgsfhksadvk
#define x1 khgrkgbdjkgbjd
#define y1 bjdlgbdfshfbvl
#define left lihfjksfhskk
#define right kgsfskgfksh
#define mod 1000000007
#define eps 1e-9
#define inf INT_MAX
#define infl LONG_LONG_MAX
#define N 100009

int Y[] = {-1,1,0,0,-1,-1,1,1};// up, down, left, right, up-left, up-right, low-left, low-right
int X[] = {0,0,-1,1,-1,1,-1,1};

int n,m,a,b,c,d,k,h,w,x,y,p,q,t,ans,res,ma,mi,T,act=0,pas=1,cur,flag,now;

int uu,vv,ww,l,r;
int dp,dp2,cnt;
char s[N];
//string s;
//vector<string> s;
double f,z,e;
vector<int> v, vec;
set<int> sett;
typedef map<int,int> Mapp;
Mapp mapp;


void input()
{
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	cin >> T;
}

inline int flip( char c )
{
	return c == '-' ? '+' : '-';
}

inline void init()
{
	ans = 0;
	c = 0;
}

inline void output()
{
	//Case #1: 3

	cout << "Case #" << ++cur << ": ";

	if( ans == 1 ) cout << "IMPOSSIBLE" << endl;

	else cout << c << endl;
}

void solve()
{
	while( T-- )
	{
		init();

		cin >> s >> k;

		n = strlen( s ) - k;

		forr(i,0,n+1)
		{
			if( s[i] == '+' ) continue;

			forr(j,i,i+k)
				s[j] = flip( s[j] );

			c++;
		}

		n = strlen( s );

		forr(i,0,n) if( s[i] != '+' ) ans = 1;

		output();
	}	
}

int main() 
{
	input();
	solve();
	//output();
	return 0;
}