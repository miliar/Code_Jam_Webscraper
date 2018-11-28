#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		double D;
		ll N;
		cin >> D >> N;

		pair<double, double> KS[N];
		for (int i = 0; i < N; i++)
			cin >> KS[i].first >> KS[i].second;

		sort(KS, KS + N);

		double time_taken = (D - KS[N - 1].first) / KS[N - 1].second;
		for (int i = N - 2; i >= 0; i--) {
			double time_needed = (D - KS[i].first) / KS[i].second;
			if (time_needed > time_taken)
				time_taken = time_needed;
		}

		printf("Case #%d: %.6lf\n", t, D / time_taken);
	}
	return 0;
}