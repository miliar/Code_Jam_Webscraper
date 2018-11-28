#include <iostream>
#include <string>

void solve() {
	std::string row;
	std::cin >> row;
	int len = row.size();
	bool pancakes[len];
	for (int i = 0; i < len; ++i) {
		pancakes[i] = row[i] == '+';
	}
	
	int flipper, max, flips = 0;
	std::cin >> flipper;
	max = len - flipper + 1;
	for (int i = 0; i < max; ++i) {
		if (!pancakes[i]) {
			++flips;
			for (int j = 0; j < flipper; ++j) {
				pancakes[i + j] = !pancakes[i + j];
			}
		}
	}
	
	bool possible = true;
	for (int i = max - 1; i < len; ++i) {
		if (!pancakes[i]) {
			possible = false;
			break;
		}
	}
	if (possible) {
		std::cout << flips;
	} else {
		std::cout << "IMPOSSIBLE";
	}
	return;
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cout << "Case #" << i + 1 << ": ";
		solve();
		std::cout << std::endl;
	}
	return 0;
}
