#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {

		cout << "Case #" << t << ": ";

		int N, K;
		cin >> N >> K;

		double U;
		cin >> U;

		double P[N];

		for (int i=0; i<N; ++i) {
			cin >> P[i];
		}

		sort(P, P+N);

		while (U > 0) {
			bool done = false;
			for (int i=1; i<N && !done; ++i) {
				if (P[i] != P[i-1]) {
					double toAdd = min(U, (P[i]-P[i-1])*i);
					for (int j=0; j<i; ++j) {
						P[j] += toAdd/i;
					}
					U -= toAdd;
					done = true;
				}
			}
			if (!done) {
				for (int j=0; j<N; ++j) {
					P[j] += U/N;
				}
				U = 0;
			}
		}

		double ans = 1;
		for (int i=0; i<N; ++i) {
			ans *= P[i];
		}

		printf("%.9f\n", ans);
	}

	return 0;
}