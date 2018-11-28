#include <bits/stdc++.h>

using namespace std;

double u; 

bool canFullfill(vector<double> &ps, double mid) {
	double curU = u;
	for (int i = 0; i < ps.size(); i++) {
		if (ps[i] < mid) {
			curU -= (mid-ps[i]);
		}
	}

	return curU >= 0;
}

int main() {
	int ntc; scanf("%d", &ntc);

	for (int tc = 0; tc < ntc; tc++) {
		int n, k; scanf("%d%d", &n, &k);
		scanf("%lf", &u);
		vector<double> ps;
		for (int i = 0; i < n; i++) {
			double p; scanf("%lf", &p);
			ps.push_back(p);
		}

		double left = 0, right = 1, mid;
		for (int i = 0; i < 100; i++) {
			mid = (left+right)/2.;
			if (canFullfill(ps, mid)) {
				left = mid;
			} else {
				right = mid;
			}
		}

		double prob = 1;
		for (int i = 0; i < ps.size(); i++) {
			if (ps[i] < mid) {
				prob *= mid;
			} else {
				prob *= ps[i];
			}
		}

		printf("Case #%d: %.8lf\n", tc+1, prob);
	}


	return 0;
}