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

typedef pair < lint , lint > pll;
typedef set < pll > spll;

typedef pair < lint, pll > plll;
typedef set < plll > splll;

typedef vector< int > vi;
typedef vector< vector < int > > vvi;
typedef vector< lint > vl;
typedef vector< vector < lint > > vvl;


const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int n, m, k;

const int MAXN = 1000 * 1 * 1 + 41;

spll s;
splll t;

void Add(lint l, lint r)
Begin
    s.insert(mp(l, r));
    t.insert(mp(l-r, mp(l,r)));
End

void Del(pll p){
s.erase(p); t.erase(mp(p.first-p.second, p));
}

void read()
{
	cin >> n >> m;
  s.clear();
 t.clear();
  Add(0, n);
}

void solve()
{
  lint ans1 = -1;
  lint ans2 = -1;
	for(int i = 0; i < m; ++i)
  {
    pll p=t.begin()->second;
    ans1 = (p.second-p.first+0)/2;
    ans2 = (p.second-p.first-1)/2;    
        
    Del(p);
        
    lint v = (p.first+p.second-1)/2;
    Add(p.first, v);
    Add(v+1, p.second);
  }
    
  cout<<ans1<<' '<<ans2;
      
}

int main()
{
	//prepare("");

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
