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

ll n,m,a,b,c,d,k,h,w,x,y,p,q,t,ans,res,ma,mi,T,act=0,pas=1,cur,flag,now;
/*
int uu,vv,ww,l,r;
int dp,dp2,cnt;
char s[1];
//string s;
//vector<string> s;
double f,z,e;
vector<int> v, vec;
set<int> sett;
*/
typedef map< ll, ll > Mapp;
Mapp mapp[100];


void input()
{
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	cin >> T;
}

inline void init()
{
	ma = 0;

	forr(i,0,77) mapp[i].clear();
}

inline void calc()
{
	forr(level,1,ma+1)
	{
		auto mapp2 = mapp[ level - 1 ];
		
		for(auto u : mapp2)
		{
			if( u.ff % 2 == 1 )
			{
				mapp[ level ][ u.ff / 2 ] += 2 * u.ss;
			}

			else
			{
				mapp[ level ][ u.ff / 2 ] += u.ss; // eg:vec.ff = 6

				mapp[ level ][ u.ff / 2 - 1 ] += u.ss;
			}
		}
		
	}

	k -= ( 1ll << ma );

	k++;

}

void solve()
{
	while( T-- )
	{
		init();

		cin >> n >> k;

		//n -= 2;

		forrev(i,62,-1)
		{
			if( k & ( 1ll << i ) )
			{
				ma = i;
				break;
			}
		}

		mapp[0][n] = 1;

		calc();

		//Case #1: 1 0

		cout << "Case #" << ++cur << ": ";

		if( mapp[ma].size() == 1 )
		{
			if( mapp[ma].begin()->ff % 2 == 1 )
				cout << mapp[ma].begin()->ff / 2 << " " << mapp[ma].begin()->ff / 2 << endl;

			else
				cout << mapp[ma].begin()->ff / 2 << " " << max( 0ll, mapp[ma].begin()->ff / 2 - 1 ) << endl;
		}

		else if( k <= mapp[ma].rbegin()->ss )
		{
			if( mapp[ma].rbegin()->ff % 2 == 1 )
				cout << mapp[ma].rbegin()->ff / 2 << " " << mapp[ma].rbegin()->ff / 2 << endl;

			else
				cout << mapp[ma].rbegin()->ff / 2 << " " << max( 0ll, mapp[ma].rbegin()->ff / 2 - 1 ) << endl;
		}

		else
		{
			if( mapp[ma].begin()->ff % 2 == 1 )
				cout << mapp[ma].begin()->ff / 2 << " " << mapp[ma].begin()->ff / 2 << endl;

			else
				cout << mapp[ma].begin()->ff / 2 << " " << max( 0ll, mapp[ma].begin()->ff / 2 - 1 ) << endl;
		}

	}
}
void output()
{
	
}

int main() 
{
	input();
	solve();
	output();
	return 0;
}