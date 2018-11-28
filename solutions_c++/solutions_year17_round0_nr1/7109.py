#include <iostream>
#include <vector>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		string S;
		int K;
		cin >> S >> K;
		int accflips = 0;
		vector<bool> flipped(S.size(), false);
		bool possible = true;
		int nFlips = 0;
		for (int i = 0; i < S.size(); ++i) {
			accflips -= (i >= K &&  flipped[i - K]) ? 1 : 0;
			if ((S[i] == '+' && accflips % 2 == 1) || (S[i] == '-' && accflips % 2 == 0)) {
				if (i <= S.size() - K) {
					flipped[i] = true;
					++accflips;
					++nFlips;
				} else {
					possible = false;
				}
			}
		}
		cout << "Case #" << test << ": ";
		if (possible) {
			cout << nFlips << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
