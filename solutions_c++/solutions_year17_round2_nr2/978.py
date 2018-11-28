#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		int n, r, y, b, o, g, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		if (2 * r > n || 2 * y > n || 2 * b > n) {
			cout << "Case #" << test << ": ";
			cout << "IMPOSSIBLE";
			cout << endl;
			continue;
		}

		vector<pair<int, char>> manes;
		manes.push_back(make_pair(-r, 'R'));
		manes.push_back(make_pair(-y, 'Y'));
		manes.push_back(make_pair(-b, 'B'));
		sort(manes.begin(), manes.end());

		string answer(n, ' ');

		for (int i = 1; i <= n; i++) {
			if (manes[0].first == 0) {
				manes[0] = manes[1];
				manes[1] = manes[2];
			}
			manes[0].first++;
			answer[(2 * n - 2 * i + ((n % 2 == 0 && 2*i <= n) ? 1 : 0)) % n] = manes[0].second;
		}

		cout << "Case #" << test << ": ";
		cout << answer;
		cout << endl;
	}
}