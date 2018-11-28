#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <iomanip>

using namespace std;
int arr[1000][2];
int main() {
	// your code goes here
	int T, D, N;
	cin >> T;
	double ans;
	
	for (int index = 1; index <= T; index++) {
		memset(arr, 0, sizeof arr);
		cin >> D >> N;
		double min = 9999999999.99999;
		double tmp;
		for ( int i = 0; i < N; i++) cin >> arr[i][0] >> arr[i][1];
		for ( int i = 0; i < N; i++ ) {
			tmp = (double) (D-arr[i][0]) / (double) arr[i][1] ;
			tmp = (double) D / tmp;
			if ( min > tmp) {
				min = tmp;
				// cout << min << endl;
			}
		}
		ans = min;
		std::cout << std::fixed;
  		std::cout << std::setprecision(6);
		cout << "Case #"<<index<<": "<<ans<<endl;
	}
	return 0;
}
