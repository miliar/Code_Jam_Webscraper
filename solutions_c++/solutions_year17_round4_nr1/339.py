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
		int N, P;
		scanf("%d%d", &N, &P);
		vector<int> G(P+1);
		for (int i = 0; i < N; ++i) {
			int g;
			scanf("%d", &g);
			++G[g % P];
		}
		int r = G[0];
		if (P == 2) {
			r += (G[1] + 1) / 2;
		} else if (P == 3) {
			int m = min(G[1], G[2]);
			r += m;
			G[1] -= m;
			G[2] -= m;
			r += (G[1] + 2) / 3 + (G[2] + 2) / 3;
		} else if (P == 4) {
			int m = min(G[1], G[3]);
			r += m;
			G[1] -= m;
			G[3] -= m;
			r += G[2] / 2;
			G[2] %= 2;
			G[1] += G[3];
			G[3] = 0;
			if (G[2] == 1 && G[1] >= 2) {
				++r;
				G[2] = 0;
				G[1] -= 2;
			}
			r += G[1] / 4;
			G[1] %= 4;
			if (G[1] != 0 || G[2] != 0) {
				++r;
			}
		}
		printf("Case #%d: %d\n", ti+1, r);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
