#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int q = 1; q <= T; ++q) {
		int N, P;
		cin >> N >> P;
		vector<int> G(N);
		for (auto& g : G) cin >> g;
		for (auto& g : G) g %= P;
		sort(G.begin(), G.end());
		int ret = 0;
		// 1-el
		while (!G.empty() && G[0] == 0) {
			++ret;
			G.erase(G.begin());
		}
		// 2-el
		while (G.size() > 1 && (G[0] + G.back()) % P == 0) {
			++ret;
			G.erase(G.begin());
			G.pop_back();
		}
		// 3-el
		while (G.size() > 2) {
			if ((G[0] + G[1] + G.back()) % P == 0) {
				++ret;
				G.erase(G.begin());
				G.erase(G.begin());
				G.pop_back();
			}
			else if ((G[0] + G[G.size()-2] + G.back()) % P == 0) {
				++ret;
				G.erase(G.begin());
				G.pop_back();
				G.pop_back();
			}
			else break;
		}
		// last
		if (!G.empty()) ++ret;

		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}