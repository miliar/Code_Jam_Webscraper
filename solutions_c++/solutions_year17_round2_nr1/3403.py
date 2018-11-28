#include<bits\stdc++.h>
using namespace std;

struct Horse {
	double K, S;
};

bool cmp(Horse a, Horse b) {
	return a.K < b.K;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, c = 1;
	cin >> t;
	while (t--) {
		int N;
		double D;
		double times[1005] = { 0 };
		Horse h[1005];
		cin >> D >> N;
		for (int i = 0; i < N; i++)
			cin >> h[i].K >> h[i].S;
		sort(h, h + N, cmp);

		double maxTime = -1;
		for (int i = N - 1; i >= 0; i--) {
			times[i] = (D - h[i].K) / h[i].S;
			for (int j = i + 1; j < N; j++) {
				if (h[i].S > h[j].S) {
					double temp = (h[j].K - h[i].K) / (h[i].S - h[j].S);
					double x = h[i].K + temp * h[i].S;
					if (x <= D) {
						times[i] = times[j];
						break;
					}
				}
			}
			maxTime = max(maxTime, times[i]);
		}

		printf("Case #%d: %lf\n", c++, D / maxTime);
	}
	return 0;
}