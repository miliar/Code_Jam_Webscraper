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

void output();

int Y[] = {-1,1,0,0,-1,-1,1,1};// up, down, left, right, up-left, up-right, low-left, low-right
int X[] = {0,0,-1,1,-1,1,-1,1};

ll n,m,a,b,c,d,k,h,w,x,y,q,t,res,ma,mi,T,act=0,pas=1,cur,flag,now;

struct node
{
	ll r,h;
};

vector< node > p;

int uu,vv,ww,l,r;
int dp,dp2,cnt;
char s[1];
//string s;
//vector<string> s;
double f,z,e, ans;
vector<double> v, vec;
set<int> sett;
typedef map<int,int> Mapp;
Mapp mapp;


void input()
{
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	cin >> T;

	cout << fixed << setprecision( 9 );
}

void init()
{
	p.clear();
	p.resize( n+1 );
	ans = 0;
	//memset( dp, 0, sizeof( dp ) );
}

bool cmp( node a, node b )
{
	if( a.r == b.r ) return a.h > b.h; // choose max height first

	return a.r > b.r;
}

double cylinder( node a )
{
	return 2 * acos( -1 ) * a.r * a.h;
}

double disk( node a )
{
	return acos( -1 ) * a.r * a.r;
}

void calc()
{
	sort( all( p ), cmp );

	//for(auto u : p) cout << u.r << " " << u.h << endl;

	forr(i,0,n)
	{
		double area = cylinder( p[i] ) + disk( p[i] );

		v.clear();

		forr(j,i+1,n)
		{
			v.pb( cylinder( p[j] ) );
		}

		sort( revall( v ) );

		if( v.size() < k - 1 ) break;

		forr(j,0,k - 1) area += v[j];

		ans = max( ans, area );
	}
}

void solve()
{
	//cout << acos( -1 ) << endl;
	while( T-- )
	{
		cin >> n >> k;

		init();

		forr(i,1,n+1)
		{
			cin >> p[i].r >> p[i].h;
		}

		calc();

		output();
	}
}
void output()
{
	//Case #1: 4 3
	cout << "Case #" << ++cur << ": " << ans << endl;
}

int main() 
{
	input();
	solve();
	//output();
	return 0;
}