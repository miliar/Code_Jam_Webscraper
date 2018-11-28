#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> r;
vector<vector<int>> q;
vector<vector<pair<int, int>>> q1;
vector<int> now;

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	cin >> tt;

	for (int t = 1; t <= tt; t++) {
		int n, p;
		cin >> n >> p;

		r = vector<int>(n, 0);
		for (int i = 0; i != n; i++) {
			cin >> r[i];
		}

		q = vector<vector<int>>(n, vector<int>(p, 0));
		for (int i = 0; i != n; i++) {
			for (int j = 0; j != p; j++) {
				cin >> q[i][j];
			}

			sort(q[i].begin(), q[i].end());
		}

		q1 = vector<vector<pair<int, int>>>(n);
		for (int i = 0; i != n; i++) {
			q1[i] = vector<pair<int, int>>(p);
			for (int j = 0; j != p; j++) {
				double normal = q[i][j] * 1.0 / r[i];
				int low = ceil(normal / 1.1);
				//int high = max(low, (int)floor(normal / 0.9));
				int high = floor(normal / 0.9);
				q1[i][j] = pair<int, int>(low, high);
			}
		}

		int valid = 0;

		now = vector<int>(n, 0);

		while (true) {
			bool success = true;
			int low = INT_MIN;
			int high = INT_MAX;
			for (int i = 0; i != n; i++) {
				for (; now[i] != p && q1[i][now[i]].second < low; now[i]++);
				if (now[i] == p) {
					success = false;
					break;
				}
				high = min(high, q1[i][now[i]].second);

				if (q1[i][now[i]].first > high) {
					//for (int k = 0; k != i; k++) {
					//	for (; now[k] != p && q1[k][now[k]].second < q1[i][now[i]].first; now[k]++);
					//}
					now[0]++;
					success = false;
					break;
				}
				low = max(low, q1[i][now[i]].first);
			}

			if (success && low <= high) {
				valid++;
				for (int i = 0; i != n; i++) {
					now[i]++;
				}
			}

			bool end = false;
			for (int i = 0; i != n; i++) {
				if (now[i] == p) {
					end = true;
					break;
				}
			}
			if (end) {
				break;
			}
		}

		printf("Case #%d: %d\n", t, valid);
	}

	fclose(stdout);
	return 0;
}
