#include <bits/stdc++.h>
using namespace std;

double solve() {
	int N, K;
	double a[64], U;
	cin >> N >> K >> U; 
	for (int i = 0; i < N; i++)
		cin >> a[i];
	sort(a, a + N);
	double cur = a[0];
	int p = 0;
	while (p < N && U > 0) {
		while (p < N && a[p] == cur) p++;
		if (p == N) break;
		double m = min(U, (a[p] - cur) * p);
		U -= m;
		for (int i = 0; i < p; i++)
			a[i] += m / p;
		cur = a[p];
	}
    for (int i = 0; i < N; i++)
			a[i] += U / N;
	double ans = 1;
	for (int i = 0; i < N; i++)
		ans *= a[i];
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		printf("%.8f\n", solve());
	}
	return 0;
}

