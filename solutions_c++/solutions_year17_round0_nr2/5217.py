#include <bits/stdc++.h>

std::string s;

void solution () {
	std::getline(std::cin, s);
	int n = s.size();

	for (int i = n - 2 ; i >= 0 ; i--) {
		if (s[i] > s[i + 1]) {
			s[i]--;
			for (int j = i + 1 ; j < n ; j++) {
				s[j] = '9';
			}
		}
	}

	while (s.size() > 1 && s[0] == '0') {
		s = s.substr(1);
	}

	std::cout << s << '\n';
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	// std::freopen("B-small-attempt0.in", "r", stdin);
	std::freopen("B-large.in", "r", stdin);

	std::freopen("B.out", "w", stdout);

	int T = 0;
	std::cin >> T;
	std::cin.ignore(10000, '\n');
	for (int i = 1 ; i <= T ; i += 1) {
		// std::cerr << "Case #" << i << "\n";
		std::cout << "Case #" << i << ": ";
		solution();
	}

	return 0;
}
