#include <bits/stdc++.h>

const int64_t maxn = 1004;

int64_t n = 0;
int64_t k = 0;
bool occupied[maxn];
int64_t ld[maxn];
int64_t rd[maxn];

void init () {
	for (int64_t i = 1 ; i <= n ; i++) {
		occupied[i] = false;
		ld[i] = -1;
		rd[i] = -1;
	}

	occupied[0] = true;
	occupied[n + 1] = true;
}

void print() {
	for (int i = 0 ; i < n + 2 ; i++) {
		std::cout << occupied[i] << ' ';
	}
	std::cout << '\n';
}

void solution () {
	std::cin >> n >> k;

	init();

	int64_t min = n + 1, max = -1;

	while (k--) {
		// print();

		for (int i = 1 ; i <= n ; i++) {
			if (occupied[i]) {
				continue;
			}

			int cld = 0;
			for (int j = i - 1 ; j >= 1 ; j--) {
				if (!occupied[j]) {
					cld++;
				} else {
					break;
				}
			}

			int crd = 0;
			for (int j = i + 1 ; j <= n ; j++) {
				if (!occupied[j]) {
					crd++;
				} else {
					break;
				}
			}

			ld[i] = cld;
			rd[i] = crd;
		}

		int in = -1;
		for (int i = 1 ; i <= n ; i++) {
			if (occupied[i]) {
				continue;
			}

			if (in == -1) {
				in = i;
				continue;
			}

			if (
				(std::min(ld[i], rd[i]) > std::min(ld[in], rd[in])) ||
				(std::min(ld[i], rd[i]) == std::min(ld[in], rd[in]) && std::max(ld[i], rd[i]) > std::max(ld[in], rd[in]))
			) {
				in = i;
			}
		}

		occupied[in] = true;
		min = std::min(ld[in], rd[in]);
		max = std::max(ld[in], rd[in]);
	}

	std::cout << max << " " << min << '\n';
}

int main () {
	// std::ios_base::sync_with_stdio(false);

	// std::freopen("x.in", "r", stdin);
	std::freopen("C-small-1-attempt0.in", "r", stdin);
	// std::freopen("C-large.in", "r", stdin);

	std::freopen("C.out", "w", stdout);

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
