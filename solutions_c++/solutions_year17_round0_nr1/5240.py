#include <bits/stdc++.h>

std::string s;
int n = 0;
int k = 0;

void solution () {
	std::cin >> s;
	n = s.size();
	std::cin >> k;

	int64_t ans = 0;

	for (int i = 0 ; i < n ; i++) {
		if (s[i] == '+') {
			continue;
		}

		ans++;

		for (int j = 0 ; j < k && i + k <= n ; j++) {
			s[i + j] = s[i + j] == '+' ? '-' : '+';
		}
	}

	for (int i = 0 ; i < n ; i++) {
		if (s[i] == '-') {
			std::cout << "IMPOSSIBLE" << '\n';
			return ;
		}
	}

	std::cout << ans << '\n';
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	// std::freopen("A-small-attempt0.in", "r", stdin);
	std::freopen("A-large.in", "r", stdin);

	std::freopen("A.out", "w", stdout);

	int T = 0;
	std::cin >> T;
	std::cin.ignore(10000, '\n');
	for (int i = 1 ; i <= T ; i += 1) {
		std::cerr << "Case #" << i << "\n";
		std::cout << "Case #" << i << ": ";
		solution();
	}

	return 0;
}
