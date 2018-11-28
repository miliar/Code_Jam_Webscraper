#include <iostream>

using namespace std;

double p[2000];

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		int n, k;
		double u;
		cin >> n >> k >> u;
		for( int i = 0; i < n; i++ )
			cin >> p[i];
		double l = 0, r = 1.;
		for( int i = 0; i < 300; i++ ){
			double mid = ( l + r ) / 2.;
			double sm = 0;
			for( int j = 0; j < n; j++ )
				if( p[j] + 1e-9 < mid )
					sm += mid - p[j];
			if( sm <= u )
				l = mid;
			else r = mid;
		}
		double res = 1.;
		for( int i = 0; i < n; i++ )
			res *= max( l, p[i] );
		cout.setf( ios::showpoint | ios::fixed );
		cout.precision( 9 );
		cout << "Case #" << T << ": " << res << endl;
	}
	return 0;
}