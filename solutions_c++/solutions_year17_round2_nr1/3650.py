#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

struct horse {
	double x, v;
	horse (double X, double V) {
		x = X,
		v = V;
	}
};

bool cmp (horse A, horse B) {
	return A.x < B.x;
}

std::vector<horse> horses;

int MaxN = 1000;

int main () {

	int t, cnt = 0;
	cin >> t;

	while (t--) {

		cnt++;

		int n;
		double d;
		double v[MaxN];
		double x[MaxN];
		cin >> d >> n;

		for (int i = 0; i < n; i++) {
			cin >> x[i] >> v[i];
			horses.push_back(horse(x[i], v[i]));
		}

		double res = 0.0;

		// if (n == 1) {
		// 	double delta_x = d - x[0];
		// 	double t = delta_x / v[0];
		// 	res = d / t;
		// } else {
		// 	double meet_point, t_1, t_2, v_final;
		// 	if (x[0] < x[1]) {
		// 		swap(v[0], v[1]);
		// 		swap(x[0], x[1]);
		// 	}
		// 	if (v[0] == v[1]) {
		// 		meet_point = d;
		// 		double min_x = min(x[0], x[1]);
		// 		res = d * v[0] / (d - min_x);
		// 	} else {
		// 		meet_point = (x[1] * v[0] - x[0] * v[1]) / (v[0] - v[1]);
		// 		t_1 = (meet_point - x[0]) / v[0];

		// 		v_final = min(v[0], v[1]);

		// 		t_2 = (d - meet_point) / v_final;

		// 		res = d / (t_1 + t_2);
		// 	}
		// }

		// sort(horses.begin(), horses.end(), cmp);

		double t = 0;

		for (int i = 0; i < n; i++) {
			t = max(t, (d - x[i]) / v[i]);
		}

		res = d / t;


		printf("Case #%d: %.6f\n", cnt, res);

	}

	return 0;
}