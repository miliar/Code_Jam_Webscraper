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

const int N = 1e6+5;

bool isTidy(ll n) {
	stringstream ss;
	ss << n;
	string num = ss.str();
	return is_sorted(num.begin(),num.end());
}

string n;
string res;

bool solve( int index, bool decreased ) {
	if ( index == n.size() )
		return is_sorted(n.begin(),n.end());
	char backup = n[index];
	if ( decreased )
		n[index] = '9';
	while ( n[index] >= 0 ) {
		if ( n[index] >= n[index-1] && solve( index + 1, decreased ) ) {
			return true;
		}
		decreased = true;
		--n[index];
	}
	n[index] = backup;
	return false;
}

int main( )
{
	int t;
	cin >> t;

	FOR(caseNr,1,t+1) {
		cout << "Case #" << caseNr << ": ";
		cin >> n;
		n = '0' + n;
		solve(1,0);
		cout << n.substr(n.find_first_not_of('0')) << endl;
	}
	return 0;
}
