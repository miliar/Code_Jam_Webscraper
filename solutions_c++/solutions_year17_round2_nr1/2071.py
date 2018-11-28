#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	cin >> tt;

	for (int t = 1; t <= tt; t++) {
		int d, n;
		cin >> d >> n;

		vector<int> position = vector<int>(n, 0);
		vector<int> speed = vector<int>(n, 0);
		for (int i = 0; i != n; i++) {
			cin >> position[i] >> speed[i];
		}

		double max_time = 0.0;
		for (int i = 0; i != n; i++) {
			double time = (d - position[i]) * 1.0 / speed[i];
			max_time = max(max_time, time);
		}

		double time = d / max_time;

		printf("Case #%d: %.6lf\n", t, time);
	}

	fclose(stdout);
	return 0;
}
