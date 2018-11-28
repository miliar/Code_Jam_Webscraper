#include <bits/stdc++.h>
#define ff first
#define ss second
#define ALL(x) (x).begin(), (x).end()
#define D(x) cout << ">> " << #x << " = >" << x << "<" << endl
#define FOR(i,a,b) for ( int i = (a); i < (b); ++i )
#define FORD(i,a,b) for ( int i = (a); i >= (b); --i )
#define PB push_back
#define R1(a) scanf( "%d", &a )
#define R2(a,b) scanf( "%d%d", &a, &b )
#define R3(a,b,c) scanf( "%d%d%d", &a, &b, &c )
#define P( cond ) \
  do \
    { \
    if ( !( cond ) ) { \
      puts( "Nespravny vstup." ); \
      return 1; \
    } \
    } while(0)
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> Matrix;

const int INF = 1e9 + 7;
const double PI = acos(-1);
const double EPS = 1e-9;

const int N = 1e3+5;
set<int> occup;
ll t, n, k;

struct cmp {
	bool operator()(const ii & a, const ii & b ) const {
		if (a.ff != b.ff)
			return a.ff < b.ff;
		return a.ss > b.ss;
	}
};

int main( )
{
	cin >> t;

	FOR(caseNr,1,t+1) {
		cout << "Case #" << caseNr << ": ";
		priority_queue<ii,vii,cmp> pq;
		cin >> n >> k;
		pq.push({n,1});
		occup.clear();
		occup.insert(0);
		occup.insert(n+1);
		int best;
		int L, R, resL, resR;
		while ( k-- ) {
			auto x = pq.top(); pq.pop();
			int beg = x.ff, end = x.ss + x.ff - 1;
			best = x.ss + (x.ff - 1) / 2;
			occup.insert(best);
			L = best-x.ss; R = x.ff-1-L;
			pq.push({L,x.ss});
			pq.push({R,best+1});
			occup.insert(best);
		}
		cout << max(L, R) << " " << min(L,R) << endl;
	}
	return 0;
}

