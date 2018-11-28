// https://code.google.com/codejam/contest/8224486/dashboard#s=p0
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdint>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int D, N;
		cin >> D >> N;
		std::vector<pair<int,int>> KS;
		for (int i = 0; i < N; i++) {
			int k, s;
			cin >> k >> s;
			KS.emplace_back(k, s);
		}
		auto solve = [&]() {
			double ans = 0;
			for (int i = 0; i < N; i++) {
				double h = (double)(D - KS[i].first) / KS[i].second;
				ans = max(ans, h);
			}
			return D / ans;
		};
		double ans = solve();
		printf("Case #%d: %.8lf\n", t, ans);
		//cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
