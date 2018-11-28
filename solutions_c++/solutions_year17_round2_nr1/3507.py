#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <iomanip>
#include <float.h>
using namespace std;

long double mymin(long double a, long double b){
	return a < b ? a : b;
}

long double max(long double a, long double b){
	return a > b ? a : b;
}

int main(void){
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; i += 1){
		int D = 0;
		cin >> D;
		int N = 0;
		cin >> N;
		vector<long double> speed = vector<long double> (N);
		for (int u = 0; u < N; u += 1){
			long double K_i, S_i;
			cin >> K_i >> S_i;
			//speed[u] = max(S_i,S_i*D/(D-K_i)));
			speed[u] = S_i/(1-K_i/D);
			//cout << "# " << speed[u] << endl;
		}
		cout << "Case #" << i << ": ";
		printf("%.*Lf\n",LDBL_DIG, *min_element(speed.begin(),speed.end()));
		//cout << setprecision (15) << *min_element(speed.begin(),speed.end());
		//cout << endl;
	}
}


