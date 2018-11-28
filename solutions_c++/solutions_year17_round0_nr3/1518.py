
#include <iostream>
#include <map>

typedef unsigned long long ull;

void add(std::map<ull, ull> &holes, ull max, ull cnt) {
	ull i = max / 2;
	if (max % 2 == 1) {
		holes[i] += 2 * cnt;
	} else {
		holes[i] += cnt;
		holes[i - 1] += cnt;
	}
}

void arrivals(std::map<ull, ull> &holes, ull count) {
	ull max = holes.rbegin()->first;
	ull mcnt = holes.rbegin()->second;
	if (mcnt > count) {
		ull red = mcnt - count;
		holes[max] -= red;
		add(holes, max, red);
	} else {
		holes.erase(max);
		add(holes, max, mcnt);
		if (count > mcnt) arrivals(holes, count - mcnt);
	}

}

int main() {
	int T;
	std::cin >> T;

	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";

		ull K, N;
		std::cin >> N >> K;

		if (K == N) {
			std::cout << "0 0";
		} else {
			std::map<ull, ull> holes;
			holes[N] = 1;
			arrivals(holes, K-1);
			ull max = holes.rbegin()->first;
			ull dist = max/2;
			if (max % 2 == 1) {
				std::cout << dist << " " << dist;
			} else {
				std::cout << dist << " " << dist - 1;
			}
		}

		std::cout << std::endl;
	}

	return 0;
}
