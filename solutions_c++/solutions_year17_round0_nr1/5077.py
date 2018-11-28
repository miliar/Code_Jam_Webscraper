#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int it = 1; it <= t; ++it) {
		string cakes;
		int k;
		cin >> cakes >> k;

		int i = 0;
		int flips = 0;
		while (i + k <= cakes.length()) {
			if (cakes[i] == '+') {
				++i;
				continue;
			}

			++flips;
			for (int j = i; j < i + k; ++j) {
				cakes[j] = (cakes[j] == '+' ? '-' : '+');
			}
			++i;
		}

		for (; i < cakes.length(); ++i) {
			if (cakes[i] != '+') {
				flips = -1;
				break;
			}
		}

		cout << "Case #" << it << ": " << (flips >= 0 ? to_string(flips) : "IMPOSSIBLE") << endl;
		cout.flush();
	}
}