#include <iostream>
#include <vector>

using namespace std;

int solve(string pancakes_raw, int k) {
	vector<bool> pancakes(pancakes_raw.size());

	for (int i = 0; i < pancakes.size(); ++i) {
		pancakes[i] = (pancakes_raw[i] == '+');
	}
	
	int flip_count = 0;
	for (int i = 0; i <= pancakes.size() - k; ++i) {
		if (pancakes[i]) {
			continue;
		}

		flip_count++;
		for (int j = 0; j < k; ++j) {
			pancakes[i+j] = !pancakes[i+j];
		}
	}

	for (int i = pancakes.size()-k; i < pancakes.size(); ++i) {
		if (!pancakes[i]) return -1;
	}

	return flip_count;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		string pancakes;
		int k;
		cin >> pancakes >> k;
		int res = solve(pancakes, k);
		cout << "Case #" << t << ": ";
		if (res != -1) {
			cout << res;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}