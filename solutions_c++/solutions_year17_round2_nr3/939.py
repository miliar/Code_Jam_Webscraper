#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <limits>

using PLL = std::pair<long long, long long>;
using VLL = std::vector<PLL>;
using VL = std::vector<long long>;
using VVL = std::vector<VL>;
using VD = std::vector<double>;
using VVD = std::vector<VD>;

long long const INF = 1000000000000LL;

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cout << std::setprecision(10);
	int T, N, Q, U, V;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		std::cin >> N >> Q;
		VL E(N), S(N);
		VVL D(N, VL(N, -1));
		VVD T(N, VD(N, (double)INF));
		for (int i = 0; i < N; ++i)
			std::cin >> E[i] >> S[i];
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				std::cin >> D[i][j];
		for (int i = 0; i < N; ++i) {
			VL dist(N, INF);
			std::priority_queue<PLL, VLL, std::greater<PLL>> max_heap;
			max_heap.emplace(0, i);
			dist[i] = 0;
			while (!max_heap.empty()) {
				PLL p = max_heap.top();
				max_heap.pop();
				int here = p.second;
				if (dist[here] != p.first) continue;
				for (int j = 0; j < N; ++j) {
					if (D[here][j] == -1) continue;
					if (dist[here] + D[here][j] < dist[j]) {
						dist[j] = dist[here] + D[here][j];
						max_heap.emplace(dist[j], j);
					}
				}
			}
			for (int j = 0; j < N; ++j) {
				if (dist[j] <= E[i]) {
					T[i][j] = dist[j];
					T[i][j] /= S[i];
				}
			}
			T[i][i] = 0.0;
		}
		for (int k = 0; k < N; ++k) {
			for (int i = 0; i < N; ++i) {
				for (int j = 0; j < N; ++j) {
					if (T[i][j] > T[i][k] + T[k][j])
						T[i][j] = T[i][k] + T[k][j];
				}
			}
		}
		std::cout << "Case #" << t << ":";
		while (Q--) {
			std::cin >> U >> V;
			std::cout << ' ' << T[U - 1][V - 1];
		}
		std::cout << std::endl;
	}
	return 0;
}
