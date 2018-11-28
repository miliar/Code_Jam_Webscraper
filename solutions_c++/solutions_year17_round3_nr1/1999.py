#include <bits/stdc++.h>
#define ff first
#define ss second
#define ALL(x) (x).begin(), (x).end()
#define D(x) //cout << ">> " << #x << " = >" << x << "<" << endl
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
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef vector<vi> Matrix;

const int INF = 1e9 + 7;
const double PI = acos(-1);
const double EPS = 1e-9;

const int N = 1e3+5;

double dp[N][N];

int t, d, n, k, s;

double surface( ll r, ll h ) {
	return h * 2 * M_PI * r + M_PI * r * r;
}

int main( )
{
	cin >> t;

	FOR(caseNr,1,t+1) {
		cin >> n >> k;
		string shit;
		FOR(i,0,k)
			shit += '1';
		FOR(i,0,n-k)
			shit += '0';
		sort(ALL(shit));
		vii p( n/* + 1*/ );
		// FOR(i,0,n+1)
		// 	FOR(j,0,n+1)
		// 		dp[i][j] = 0;
		// FOR(i,1,n+1)
		FOR(i,0,n)
			cin >> p[i].ff >> p[i].ss;
		sort( ALL(p) );
		reverse(ALL(p));
		double best = 0;
		do {
			bool first = true;
			double res = 0;
			FOR(i,0,n) {
				if ( shit[i] == '1' ) {
					if ( first )
						res = surface( p[i].ff, p[i].ss );
					else
						res = res + surface( p[i].ff, p[i].ss ) - M_PI * p[i].ff * p[i].ff;
					first = false;
				}
			}
			best = max( best, res );
		} while ( next_permutation( ALL(shit)));

		// FOR(i,1,n+1) {
		// 	dp[i][1] = max( surface( p[i].ff, p[i].ss ), dp[i-1][1] );
		// 	FOR(j,1,k+1) {
		// 		dp[i+1][j+1] = max( dp[i+1][j+1], dp[i][j] + surface( p[i+1].ff, p[i+1].ss ) - M_PI * p[i].ff * p[i].ff );
		// 		dp[i+1][j]   = max( dp[i+1][j], dp[i][j] );
		// 	}
		// }
		// FOR(i,0,n+1) {
		// 	FOR(j,0,n+1)
		// 		cout << dp[i][j] << " ";
		// 	cout << endl;
		// }
		
			
		printf("Case #%d: %.8f\n", caseNr, best);
//		cout << "Case #" << caseNr << ": " << setprecimaxSpeed << endl;
	}
	return 0;
}
