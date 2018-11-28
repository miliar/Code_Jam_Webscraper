#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large-0.out", "w", stdout);
	int q;
	cin >> q;
	double pi = atan(1)*4;
	//cout << pi << endl;
	for (int tc= 1; tc <= q; tc++) {
		int n,k;
		int r[1005];
		int h[1005];
		double maxa = 0;
		double area[1005];
		for (int i = 0; i < 1005; i++) {
			area[i] = 0.0;
		}
		double ans = 0;
		cin >> n >> k;
		for (int i = 0; i < n ;i ++) {
			int ra, ha;
			scanf("%d %d", &ra, &ha);
			r[i] = ra;
			h[i] = ha;
			
			area[i] = 2.0 * pi * (double) ra * (double) ha;
			//cout << area[i] << endl;
		}
		for (int i = 0; i < n; i++) {
			double ans = 0.0;
			ans += pi * (double)r[i] * (double)r[i];
			ans += area[i];
			double temp[1005];
			//area[i] = 0.0;
			for (int j = 0; j < n; j++) {
				if (j == i) temp[j] = 0;
				else temp[j] = area[j];
			}
			sort(temp, temp+n);
			reverse(temp, temp+n);
			for (int j = 0; j < k-1; j++) {
				ans += temp[j];
			}
			maxa = max(ans, maxa);
		}	
		//ans += pi * cake[0] * cake[0];
		printf("Case #%d: %.8f\n", tc, maxa);
	}
}
