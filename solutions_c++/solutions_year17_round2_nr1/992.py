#include <bits/stdc++.h>

using namespace std;

#define PB push_back
#define MP make_pair
#define X first
#define Y second

int main(){
	cout.setf( ios::fixed );
	cout.precision( 8 );
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		double D, N; cin >> D >> N;
		double maxi = 0.0;
		for( int n = 0; n < N; n++ ){
			double K, S; cin >> K >> S;
			maxi = max( maxi, (D-K)/(S) );
		}
		cout << "Case #" << kase <<": "<<(D/maxi)<<endl;	
	}
}
