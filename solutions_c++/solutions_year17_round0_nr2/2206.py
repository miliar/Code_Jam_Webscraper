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

ll n,m,a[100],b,c,d,k,h,w,x,y,p,q,t,ans,res,ma,mi,T,act=0,pas=1,cur,flag,now,idx;
/*
int uu,vv,ww,l,r;
int dp,dp2,cnt;
char s[1];
//string s;
//vector<string> s;
double f,z,e;
vector<int> v, vec;
set<int> sett;
typedef map<int,int> Mapp;
Mapp mapp;
*/

void input()
{
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	cin >> T;
}

inline void init()
{
	n = 0;
	m = 0;
	c = 0;
	ans = 0;
	memset( a, 0, sizeof( a ) );
}

inline void putinarray()
{
	c = 0;

	m = n;

	while( m )
	{
		c++; m /= 10;
	}

	a[ 0 ] = 0;

	m = n;

	d = c;

	while( m )
	{
		a[ d-- ] = m % 10;

		m /= 10;
	}

	c++;
}

inline bool isvalid()
{
	forr(i,1,c)
	{
		if( a[i-1] > a[i] ) return false;
	}

	return true;
}

inline void modify()
{
	forr(i,1,c)
	{
		if( a[i-1] > a[i] )
		{
			a[i-1]--;

			forr(j,i,c)
				a[j] = 9;
		}
	}
}

void print()
{
	forr(i,0,c)cout<<a[i]; cout << endl;
}

void solve()
{
	while( T-- )
	{
		init();

		cin >> n;

		putinarray();

		//print();

		while( !isvalid() )
		{
			modify();

			//print();
		}

		forr(i,0,c) ans = ans * 10 + a[i];

		cout << "Case #" << ++cur << ": " << ans << endl;
	}
}

int main() 
{
	input();
	solve();
	//output();
	return 0;
}