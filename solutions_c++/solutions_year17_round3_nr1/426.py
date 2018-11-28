#include <bits/stdc++.h>
using namespace std;

const double pi = acos(-1);

int T, N, K;
pair <double, double> C[1005];

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d", &N, &K);
		for(int i = 0; i < N; i++)
			scanf("%lf %lf", &C[i].first, &C[i].second);
		sort(C, C + N);

		double res = 0.0;
		for(int i = K - 1; i < N; i++){
			double r = 0.0;

			r += pi * C[i].first * C[i].first;
			r += 2 * pi * C[i].first * C[i].second;

			vector <double> v;
			for(int j = 0; j < i; j++)
				v.push_back(2 * pi * C[j].first * C[j].second);
			sort(v.rbegin(), v.rend());

			for(int j = 0; j < K - 1; j++)
				r += v[j];

			res = max(res, r);
		}
		printf("Case #%d: %.9f\n", t, res);
	}
	return 0;
}
