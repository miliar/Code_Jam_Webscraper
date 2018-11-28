#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int flipCount(vector<bool>& bits, int K) {
	int high = bits.size();
	int flips = 0;
	while (true) {
		do {
			high--;
		} while (high >= 0 && bits[high] == 0);
		if (high == -1)
			return flips;
		if (high < K - 1)
			return -1;

		for (int i = 0; i < K; i++) {
			bits[high - i] = !bits[high - i];
		}
		flips++;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		// read input
		string S;
		int K;
		cin >> S >> K;
		vector<bool> bits;
		for (char c : S)
			bits.push_back(c == '-');

		cout << "Case #" << t + 1 << ": ";

		int c = flipCount(bits, K);
		if (c == -1)
			cout << "IMPOSSIBLE";
		else
			cout << c;

		cout << endl;
	}
}