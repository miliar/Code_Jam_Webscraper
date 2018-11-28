#include <algorithm>
#include <cctype>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <stack>
#include <string>
#include <strstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
typedef int64_t i64;
typedef double dbl;

int main(int argc, char** argv) {
	if (argc == 2) {
		freopen(argv[1], "r", stdin);
	}
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		int N, C, M;
		scanf("%d%d%d", &N, &C, &M);
		vector<vector<int>> B(C, vector<int>(N));
		vector<int> count(C);
		vector<int> total(N);
		for (int i = 0; i < M; ++i) {
			int p, b;
			scanf("%d%d", &p, &b);
			--b;
			--p;
			++B[b][p];
			++count[b];
			++total[p];
		}
		int l = *max_element(count.begin(), count.end()) - 1;
		int r = M;
		int rides = M;
		int bestPromo = 0;
		while (r > l + 1) {
			int m = (l + r + 1) / 2;
			bool flag = true;
			int promo = 0;
			int reserve = 0;
			for (int p = 0; p < N; ++p) {
				if (total[p] <= m) {
					reserve += m - total[p];
				} else if (total[p] <= m + reserve) {
					int d = total[p] - m;
					promo += d;
					reserve -= d;
				} else {
					flag = false;
					break;
				}
			}
			if (!flag) {
				l = m;
			} else {
				r = m;
				rides = m;
				bestPromo = promo;
			}
		}
		printf("Case #%d: %d %d\n", ti+1, rides, bestPromo);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
