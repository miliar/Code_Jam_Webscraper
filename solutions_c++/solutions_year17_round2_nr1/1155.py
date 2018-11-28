#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int _t = 1; _t <= T; _t++){
		double k;
		int d;
		cin >> k >> d;
		double t = 0;
		for(int i =0 ; i < d; i++){
			double p;
			double s;
			cin >> p >> s;
			double tt = (k - p) / s;
			t = max(t, tt);
			// cout << t << endl;
		}
		printf("Case #%d: %.9lf\n", _t, k / t);
	}
	return 0;
}