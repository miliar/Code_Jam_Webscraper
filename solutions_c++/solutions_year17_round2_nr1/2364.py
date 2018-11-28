#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int cnt = 1; cnt <= t; cnt++) {
		long long d, n, k, s;
		double ans, h = 0;
		cin >> d >> n;
		for (int i = 0; i < n; i++) {
			cin >> k >> s;
			if (h < (double)(d - k) / s) h = (double)(d - k) / s;
		}
		ans = d / h;
		cout << "Case #" << cnt << ": ";
		printf("%.6f\n", ans);
	}
	return 0;
}
