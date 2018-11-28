#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main(){

	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		double D, n; cin >> D >> n;
		double max_t = 0;
		for(int i = 0; i < n; i++){
			double p, s; cin >> p >> s;
			double t = (D - p) / s;
			if(t > max_t){
				max_t = t;
			}
		}

		printf("Case #%d: %.7f\n", tc, D/max_t);
	}
}
