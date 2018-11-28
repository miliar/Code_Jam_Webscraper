#include <queue>
#include <iostream>

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int T, k;
	string pancakes;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		bool possible = true;
		int steps = 0;
		cin >> pancakes;
		cin >> k;
		queue<int> flips;
		for (int i = 0; i < pancakes.size() && possible; i++) {
			if (!flips.empty() && flips.front() <= i) {
				flips.pop();
			}
			if ((pancakes[i] == '-' && flips.size() % 2 == 0) || (pancakes[i]
					== '+' && flips.size() % 2 == 1)) {
				if (i + k <= pancakes.size()) {
					steps++, flips.push(i + k);
				} else
					possible = false;
			}
		}
		if (possible) {
			printf("Case #%i: %i\n", t + 1, steps);
		} else {
			printf("Case #%i: IMPOSSIBLE\n", t + 1);
		}
	}
	return 0;
}
