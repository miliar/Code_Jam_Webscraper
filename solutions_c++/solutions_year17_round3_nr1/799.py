#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);

		int N, K;
		cin >> N >> K;
		vector<pair<double,double>> RH(N);
		for (int i = 0; i < N; i++) {
			cin >> RH[i].first >> RH[i].second;
		}
		sort(RH.rbegin(), RH.rend());

		const double pi = acos(-1);
		double ans = 0.0;
		for (int i = 0; i <= N-K; i++) {
			double area = RH[i].first * RH[i].first * pi;
			area += 2 * RH[i].first*pi*RH[i].second;
			vector<double> v;
			for (int j = i+1; j < N; j++) {
				v.push_back(2 * RH[j].first*pi*RH[j].second);
			}
			sort(v.rbegin(), v.rend());
			for (int j = 0; j < K-1; j++) {
				area += v[j];
			}
			ans = max(ans, area);
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
