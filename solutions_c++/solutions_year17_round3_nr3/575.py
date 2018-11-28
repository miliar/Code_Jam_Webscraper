#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("readin.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	while (t--) {

		int n, k;
		scanf("%d%d", &n, &k);
		double a, u;
		cin >> u;
		priority_queue<double> q;
		for (int i = 0; i < n; i++) {
			scanf("%lf", &a);
			q.push(-a);
		}
		while (u > 0.00005 && q.size()) {
			double a = -q.top();
			q.pop();
			u -= 0.0001;
			if (a + 0.0001 == 1 || (fabs((a + 0.0001) - 1) < 1e-12)) continue;
			a += 0.0001;
			q.push(-a);
		}
		double ans = 1;
		while (!q.empty()) {
			ans *= -(q.top());
			q.pop();
		}
		static int tc = 1;
		printf("Case #%d: ", tc++);
		cout << fixed << setprecision(6) << ans << endl;
	}

	return 0;
}
