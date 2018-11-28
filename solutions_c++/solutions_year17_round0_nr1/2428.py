#include <iostream>
#include <string>
#include <vector>

int main() {
	std::ios_base::sync_with_stdio(false);
	int T, K;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		std::string S;
		std::cin >> S >> K;
		std::vector<int> V(S.size()), E(S.size() + 1, 0);
		for (int i = 0; i < S.size(); ++i)
			V[i] = (S[i] == '+' ? 1 : 0);
		int ans = 0, f = 0;
		for (int i = 0; i < S.size(); ++i) {
			f ^= E[i];
			if (V[i] ^ f == 0) {
				if (i + K <= S.size()) {
					++ans;
					f ^= 1;
					E[i + K] = 1;
				} else {
					ans = -1;
					break;
				}
			}
			V[i] ^= f;
		}
		std::cout << "Case #" << t << ": ";
		if (ans > -1) std::cout << ans;
		else std::cout << "IMPOSSIBLE";
		std::cout << std::endl;
	}
	return 0;
}