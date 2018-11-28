#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

bool IsEmpty(std::string cakeRow) {
	auto nonempty = std::count_if(cakeRow.begin(), cakeRow.end(), [](auto c) {
		return c != '?';
	});
	return nonempty == 0;
}

int main(int argc, char** argv) {
	int T;
	std::cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		std::cout << "Case #" << tc << ":\n";
		int R, C;
		std::cin >> R >> C;
	
		std::vector<std::string> CAKE;
		for (int i = 0; i < R; i++) {
			std::string ROW;
			std::cin >> ROW;
			CAKE.push_back(ROW);
		}

		int r = 0;
		while (r < R) {
			int rNext = r;
			while (rNext < R && IsEmpty(CAKE[rNext])) {
				rNext++;
			}
			if (rNext == R) {
				for (int i = r; i < R; i++) {
					CAKE[i] = CAKE[r - 1];
				}
				break;
			}
			else {
				int c = 0;
				while (c < C) {
					int cNext = c;
					while (cNext < C && CAKE[rNext][cNext] == '?') {
						cNext++;
					}
					if (cNext == C) {
						for (int i = c; i < C; i++) {
							CAKE[rNext][i] = CAKE[rNext][c - 1];
						}
						break;
					}
					for (int i = c; i < cNext; i++) {
						CAKE[rNext][i] = CAKE[rNext][cNext];
					}
					c++;
				}
				for (int i = r; i < rNext; i++) {
					CAKE[i] = CAKE[rNext];
				}
			}
			r++;
		}
		for (int i = 0; i < R; i++) {
			std::cout << CAKE[i] << '\n';
		}
	}

	return 0;
}