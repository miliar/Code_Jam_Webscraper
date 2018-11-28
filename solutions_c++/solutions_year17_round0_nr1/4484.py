#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <deque>
#include <stack>

#include <cmath>
#include <string>

#include <cassert>
#include <time.h>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

#define fi(n) for (int i = 0; i < (n); ++ i)
#define fj(n) for (int j = 0; j < (n); ++ j)
#define fin() for (int i = 0; i < n; ++ i)
#define fjm() for (int j = 0; j < m; ++ j)
#define forv(i, v) for (int i = 0; i < sz((v)); ++ i)

#define Begin {
#define End   }

#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef long double ld;

typedef vector< int > vi;
typedef vector< vector < int > > vvi;
typedef vector< lint > vl;
typedef vector< vector < lint > > vvl;


const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	if (sz(s) > 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

int n, m, k;
string s;
const int MAXN = 1000 * 1 * 1 + 41;

void read()
{
	cin>>s>>n;
}


void swp(char &c)
Begin
   if (c=='-')
      c='+';
    else
      c='-';
End
void solve()
{
  int ans=0;
	for(int i =0; i<sz(s)-n+1;++i) Begin
    if (s[i]=='-')Begin
       for (int j=0; j<n; ++j)
          swp(s[i+j]);
       ++ans;
    End
  End
    
  if (s.find('-')!=-1) 
    cout << "IMPOSSIBLE";
  else
    cout<<ans;
    
}

int main()
{
	prepare("");

	int T;
	cin >> T;
	fi(T)
	{
  
		read();
		cout << "Case #" << i + 1 << ": ";
		cerr << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
		cerr << endl;
	}

	return 0;
}
