#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		int n;
		double d;
		cin >> d >> n;
		double time;
		for (int i = 0; i < n; ++i) {
			double p, v;
			cin >> p >> v;
			double cur_time = (d - p) / v;
			if (i == 0 || cur_time > time)
				time = cur_time;
		}
		printf("Case #%d: %.9lf\n", t, d / time);
	}
}