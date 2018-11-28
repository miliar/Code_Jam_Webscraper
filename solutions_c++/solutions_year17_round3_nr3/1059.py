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

const int N = 55;

int t, d, n, k, s;

int main( )
{
	double u;
	cin >> t;

	FOR(caseNr,1,t+1) {
		cin >> n >> k >> u;
		vector<double> cores(n);
		cores.PB(1);
		FOR(i,0,n)
			cin >> cores[i];
		sort(ALL(cores));
		FOR(i,0,n) {
			// D(cores[i+1]);
			double need = (cores[i+1] - cores[i]) * (i+1);
			double add  = min( need, u );
			FOR(j,0,i+1)
				cores[j] += add / (i+1);
			u -= add;
		}
		double p = 1;
		FOR(j,0,n)
			p *= cores[j];
		printf("Case #%d: %.8f\n", caseNr, p);
	}
	return 0;
}
