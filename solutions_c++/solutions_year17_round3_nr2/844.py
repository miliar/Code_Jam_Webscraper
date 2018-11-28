#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int task() {
	int a1, a2;
	cin >> a1 >> a2;
	vector<pair<int, int> > v1, v2;
	for (int i = 0; i < a1; ++i) {
		int pom1, pom2; cin >> pom1 >> pom2;
		v1.push_back(make_pair(pom1, pom2));
	}
	for (int i = 0; i < a2; ++i) {
		int pom1, pom2; cin >> pom1 >> pom2;
		v2.push_back(make_pair(pom1, pom2));
	}
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());

	if (a1 + a2 <= 2) {
		if (a1 + a2 < 2) return 1;
		if (a1 == 1 && a2 == 1) return 1;
		if (a1 == 0) swap(v1, v2);
		if (v1[1].second - v1[0].first <= 12 * 60 || v1[0].second + 24 * 60 - v1[1].first <= 12 * 60)
			return 1;
		return 2;
	}
	return 0;
}


int main() {
	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {

		cout << "Case #" << tst << ": " << task() * 2<< "\n";
	}
	return 0;
}