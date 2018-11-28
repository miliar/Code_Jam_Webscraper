#include<bits\stdc++.h>
using namespace std;

int main() {

	freopen("C-small-1-attempt1.in", "r", stdin);
	//freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, c = 1;
	cin >> t;
	while (t--) {
		double ans = 1;
		int N, K;
		double U;
		double p[55];
		cin >> N >> K >> U;
		for (int i = 0; i < N; i++)
			cin >> p[i];
		sort(p, p + N);

		double sum = 0;
		for (int i = 0; i < N; i++)
			ans *= p[i];
		for (int i = 0; i < N; i++) {
			double baseline = p[i];
			double temp = 1;
			sum += p[i];

			double s = (U + sum) / (i + 1);
			if (s < baseline)
				break;

			for (int j = 0; j < N; j++) {
				if (j <= i)
					temp *= min(1.0, s);
				else
					temp *= p[j];
			}
			ans = max(ans, temp);
		}

		printf("Case #%d: %.8lf\n", c++, ans);
	}

	return 0;
}