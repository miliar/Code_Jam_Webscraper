#include <bits/stdc++.h>


const int maxn = 100;

int ac = 0, aj = 0;
std::pair<int, int> cameron[maxn];
std::pair<int, int> jamie[maxn];

void init () {}

void solution () {
	std::cin >> ac >> aj;

	for (int i = 0 ; i < ac ; i++) {
		int start = 0, end = 0;
		std::cin >> start >> end;
		cameron[i] = {start, end};
	}

	for (int i = 0 ; i < aj ; i++) {
		int start = 0, end = 0;
		std::cin >> start >> end;
		jamie[i] = {start, end};
	}

	// init();

	if ((ac == 0 && aj == 1) || (ac == 1 && aj == 0)) {
		std::cout << 2 << '\n';
		return ;
	}

	if (ac == 1 && aj == 1) {
		std::cout << 2 << '\n';
		return ;
	}

	std::sort(cameron, cameron + ac);
	std::sort(jamie, jamie + aj);

	if (ac == 2) {
		if (cameron[1].second - cameron[0].first <= 720) {
			std::cout << 2 << '\n';
		} else if (cameron[0].second + 1440 - cameron[1].first <= 720) {
			std::cout << 2 << '\n';
		} else {
			std::cout << 4 << '\n';
		}
		return ;
	}

	if (jamie[1].second - jamie[0].first <= 720) {
		std::cout << 2 << '\n';
	} else if (jamie[0].second + 1440 - jamie[1].first <= 720) {
		std::cout << 2 << '\n';
	} else {
		std::cout << 4 << '\n';
	}
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	// std::freopen("B-small-attempt0.in", "r", stdin);
	// std::freopen("B-small-attempt1.in", "r", stdin);
	// std::freopen("B-small-attempt2.in", "r", stdin);
	std::freopen("B-small-attempt3.in", "r", stdin);
	// std::freopen("B-large.in", "r", stdin);

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
