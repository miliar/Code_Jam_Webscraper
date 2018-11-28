#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
const int maxn = 55;
int main() {
	int T; cin >> T;

	for(int tt = 1; tt <= T; tt++) {
		int n, k;
		cin >> n >> k;
		double x; cin >> x;
		double p[maxn];
		
		for(int i = 0; i < n; i++) cin >> p[i];
		sort(p, p+n);
		//for(int i = 0; i < n; i++) cout << p[i] << endl;
		for(int i = 0; i < n-1; i++) {
			double d = (p[i+1] - p[i]);
			if(d * (i+1) <= x) x -= d * (i+1);
			else d = x/(double)(i+1), x = 0.0;
		//	cout << x << d << endl;
			for(int j = 0; j <= i; j++) p[j] += d;
		//	for(int j = 0; j < n; j++) cout << p[j] << endl;
		//	cout << endl;
		}
		for(int i = 0; i < n; i++) p[i] += (x/n);
		double ans = 1.0;
		for(int i = 0; i < n; i++) {
			ans *= p[i];
		//	cout << p[i] << endl;
		}
		printf("Case #%d: %.6lf\n", tt, ans);
		//cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}
