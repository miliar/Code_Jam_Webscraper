#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

bool p[1 << 11];

int main() {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		for (int i = 0; i < 1 << 11; ++i) p[i] = false;
		std::string S; std::cin >> S;
		int K; std::cin >> K;
		int n = 0;
		int s = S.size();
		int f = (1 << K) - 1;
		for (unsigned int i = 0; i < s; ++i) if (S[i] == '+') n |= (1 << i);
		// std::cout << S << '\n';
		// std::cout << n << '\n';
		// std::cout << f << '\n';
		// std::cout << (1 << s) - 1 << '\n';
		std::queue<int> q;
		std::queue<int> z;
		z.push(n);
		int c = 0;
		int r = -1;
		while (!z.empty()) {
			std::swap(q, z);
			c += 1;
			while (!q.empty()) {
				n = q.front();
				q.pop();
				if (n == ((1 << s) - 1) && r == -1) r = c;
				if (!p[n]) {
					p[n] = true;
					for (int i = 0; i <= s - K; ++i) {
						z.push(n ^ (f << i));
					}
				}
			}
		}
		std::cout << "Case #" << t << ": ";
		if (r != -1) std::cout << (r - 1) << '\n';
		else std::cout << "IMPOSSIBLE\n";
	}
}
