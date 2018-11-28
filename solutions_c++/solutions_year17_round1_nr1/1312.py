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
char s[109][109];
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

void calc()
{
	forr(col,0,n)
	{
		forr(row,1,m)
		{
			if( s[row-1][col] != '?' && s[row][col] == '?' )
				s[row][col] = s[row-1][col];
		}

		forrev(row,m-2,-1)
		{
			if( s[row+1][col] != '?' && s[row][col] == '?' )
				s[row][col] = s[row+1][col];
		}
	}

	forr(row,0,m)
	{
		forr(col,1,n)
		{
			if( s[row][col-1] != '?' && s[row][col] == '?' )
				s[row][col] = s[row][col-1];
		}

		forrev(col,n-2,-1)
		{
			if( s[row][col+1] != '?' && s[row][col] == '?' )
				s[row][col] = s[row][col+1];
		}
	}
}

void solve()
{
	while( T-- )
	{
		cin >> m >> n;

		forr(i,0,m) cin >> s[i];

		calc();

		//Case #1:
		cout << "Case #" << ++cur << ":" << endl;

		forr(i,0,m) cout << s[i] << endl;
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