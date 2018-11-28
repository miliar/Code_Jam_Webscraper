#include <iostream>
#include <algorithm>
#define MAXN 2000
#define P pair< double, double >

using namespace std;

P p[MAXN];
double q[MAXN];
double PI = acos( -1. );

int main()
{
	int n, k, test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> n >> k;
		double res = 0;
		for( int i = 0; i < n; i++ )
			cin >> p[i].second >> p[i].first;
		for( int i = 0; i < n; i++ ){
			int pt = 0;
			for( int j = 0; j < n; j++ )
				if( i != j && p[j].second <= p[i].second )
					q[pt++] = 2. * PI * p[j].first * p[j].second;
			//cerr << pt << endl;
			if( pt < k - 1 )
				continue;
			sort( q, q + pt );
			double curRes = PI * p[i].second * p[i].second + 2. * PI * p[i].first * p[i].second;
			cerr << curRes / PI << endl;
			for( int j = pt - 1; j > pt - k; j-- )
				curRes += q[j];
			//cerr << curRes / PI << endl;
			res = max( res, curRes );
		}
		cout.setf( ios::showpoint | ios::fixed );
		cout.precision( 9 );
		cout << "Case #" << T << ": " << res << endl;
	}

	return 0;
}