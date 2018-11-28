#include <bits/stdc++.h>
#include <map>
using namespace std;

int main() {
	int T;
	long long n, k;

	cin >> T;

	for (int t=1 ; t<=T ; ++t) {
		cin >> n >> k;
		int a , b ; 
		double max = 0.000000 ;
		for ( int i=1; i<=k; ++i ) {
			cin >> a >> b ; 
			double temp = ((n-a)*(1.000000))/(b*(1.000000)) ;
			if ( temp > max ) {
				max = temp ;
			}
		}
		double y = (n*(1.000000))/(max)*(1.000000) ;
		cout << "Case #" << t << ": " ;
		printf("%.6lf\n",y );
	}

	return 0;
}