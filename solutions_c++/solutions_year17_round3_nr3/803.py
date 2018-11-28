#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		int n, k; cin >> n >> k;
		double u; cin >> u;
		double p[n];
		for(int i = 0; i < n; i++) cin >> p[i];

		sort(p, p+n);
		int i = 1;
		double prev = p[0];
		while(i <= n){

			double cur = p[i];
			if(prev == cur) {
				i++;
				continue;
			}

			double max_req = (i) * (cur - prev);
			if(max_req > u){
				double z = u / i;
				for(int j = 0; j < i; j++){
					p[j] += z;
					u -= z;
				}
			}else{

				double s = (cur - prev);
				for(int j = 0; j < i; j++){
					p[j] += s;
					u -= s;
				}
			}
			i++;
			prev = cur;
		}

		double rem = u / (n);
		for(int i = 0; i < n; i++) {
			p[i] += rem;
			//cout << p[i] << ", ";
		}

		double ans = 1.0;
		for(int i = 0; i < n; i++) ans *= p[i];

		printf("Case #%d: %.7f\n", tc, ans);
	}
	return 0;

}