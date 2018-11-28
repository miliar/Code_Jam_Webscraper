#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <stdint.h>
#include <string>
#include <utility>
#include <vector>
#include <iostream>

using namespace std;

void solve(int t) {
	int N, C, M;
	cin >> N >> C >> M;
	vector<vector<int> > places(C);
	for (int i = 0; i < C; ++i) {
		places[i].resize(N);
	}
	if (t == 18) {
		cout << "";
	}
	int ones = 0, c1=0, c2=0;
	for (int i = 0; i < M; ++i) {
		int p, b;
		cin >> p >> b;
		places[b - 1][p - 1]++;
		if (b == 1) c1++;
		else c2++;
	}

	int pl = 0, prom = 0;
	int onesFirst = places[0][0];

	for (int it = 0; it < onesFirst; ++it) {
		pl++;
		--c1;

		if (c2 - places[1][0] == 0)
			continue;
		int index = -1, maxch = 0;
		for (int i = 1; i < N; ++i) {
			if (maxch < places[0][i] + places[1][i]) {
				maxch = places[0][i] + places[1][i];
				index = i;
			}
		}
		if (index == -1) {
			continue;
		}
		else {
			--places[1][index];
		}
		--c2;
	}
	places[0][0] = 0;

	int onesSecond = places[1][0];

	for (int it = 0; it < onesSecond; ++it) {
		pl++;
		--c2;
		if (c1 == 0)
			continue;
		int index = -1, maxch = 0;
		for (int i = 1; i < N; ++i) {
			if (maxch < places[0][i] + places[1][i]) {
				maxch = places[0][i] + places[1][i];
				index = i;
			}
		}
		--places[0][index];
		--c1;
	}
	places[1][0] = 0;

	pl += max(c1, c2);
	int maxChSum = 0;
	for (int i = 0; i < N; ++i) {
		maxChSum = max(maxChSum, places[0][i] + places[1][i]);
	}
	prom = max(0, maxChSum - max(c1, c2));

	printf("Case #%d: %d %d\n", t, pl, prom);
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}
