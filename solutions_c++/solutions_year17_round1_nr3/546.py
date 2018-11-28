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

const int N = 1e2;

ll needed[N];
ll got[N][N];
bool available[N][N];
bool ispackage[N][N];
int n, p;

struct state {
	state( int ad, int ak, int hd, int hk, int dist ) : ad(ad), ak(ak), hd(hd), hk(hk), dist(dist){}
	bool operator<(const state & s) const {
		return tie(ad,ak,hd,hk) < tie(s.ad,s.ak,s.hd,s.hk);
	}
	int ad, ak, hd, hk, dist;
};

int main( )
{
	int t, hd, ad, hk, ak, b, d;
	cin >> t;

	FOR(caseNr,1,t+1) {
		cin >> hd >> ad >> hk >> ak >> b >> d;
		cout << "Case #" << caseNr << ": ";
		queue<state> q;
		set<state> visited;
		q.push( state( ad, ak, hd, hk, 0 ));
		while ( !q.empty( ) ) {
			auto u = q.front(); q.pop();
			//cout << "ad: " << u.ad << ", ak: " << u.ak << ", hd: " << u.hd << ", hk: " << u.hk << ", dist: " << u.dist << endl;
			if ( u.hk <= 0 ) {
				cout << u.dist << endl;
				goto next;
			}
			if ( u.hd <= 0 || visited.count(u))
				continue;
			visited.insert(u);
			q.push( state( u.ad, u.ak, u.hd - u.ak, u.hk - u.ad, u.dist + 1 ) );
			q.push( state( u.ad + b, u.ak, u.hd - u.ak, u.hk, u.dist + 1 ) );
			q.push( state( u.ad, u.ak, hd - u.ak, u.hk, u.dist + 1 ) );
			q.push( state( u.ad, max( u.ak - d, 0 ), u.hd - max( 0, u.ak - d), u.hk, u.dist + 1 ) );
		}
		cout << "IMPOSSIBLE" << endl;
		next:;
	}
	return 0;
}
