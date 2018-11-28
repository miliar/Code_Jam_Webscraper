#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <numeric>
#include <queue>
#include <cassert>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef double ld;

#define TASK "divisible"

int solve();

int main() {
#ifdef PoDuReM
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	return solve();
}

const int dd = (int)1e3 + 1;

int L[dd], R[dd];

int solve() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		int Ac, Aj;
		scanf("%d %d", &Ac, &Aj);
		for (int i = 0; i < Ac + Aj; ++i)
			scanf("%d %d", &L[i], &R[i]);
		if (Ac + Aj <= 1) {
			puts("2");
			continue;
		}
		if (Ac < Aj) swap(Ac, Aj);
		if (Ac == 1 && Aj == 1)
			puts("2");
		else {
			if (L[0] > L[1])
				swap(L[0], L[1]), swap(R[0], R[1]);
			int K = R[1] - L[0];
			if (K <= 720) puts("2");
			else if (1440 - K + R[0] - L[0] + R[1] - L[1] <= 720) puts("2");
			else puts("4");
		}
	}

	return 0;
}