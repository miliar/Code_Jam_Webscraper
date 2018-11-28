#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		int N, P; cin >> N >> P;
		vector<int> groups(5);
		for (int i = 0; i < N; ++i) {
			int x; cin >> x; x %= P;
			groups[x]++;
		}

		int best = 0;
		int x;
		switch (P) {
		case 2:
			best = groups[0] + (groups[1] + 1) / 2;
			break;
		case 3:
			best = groups[0];
			x = min(groups[1], groups[2]);
			best += x;
			groups[1] -= x;
			groups[2] -= x;
			best += (groups[1] + groups[2] + 2) / 3;
			break;
		case 4:
			break;
		}

		cout << "Case #" << test << ": " << best << endl;
	}
	return 0;
}