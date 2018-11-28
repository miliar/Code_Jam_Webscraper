#define _CRT_SECURE_NO_WARNINGS
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
#include <random>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TASK "connect"

int solve();

int main() {
#ifdef PoDuReM
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	return solve();
}

const int dd = (int)1e3 + 7;
const int inf = (int)1e9 + 7;

char s[dd];

void get(int i, int n) {
	if (i == n) return;
	int ok = 1;
	for (int j = i; j < n; ++j) {
		if (s[j] > s[i]) break;
		if (s[j] < s[i]) {
			ok = 0;
			break;
		}
	}
	if (ok) printf("%c", s[i]), get(i + 1, n);
	else {
		s[i]--;
		if (s[i] != '0' || i != 0)
			printf("%c", s[i]);
		for (int j = i + 1; j < n; ++j)
			printf("9");
	}
}

int solve() {
	int T;
	scanf("%d\n", &T);
	for (int it = 1; it <= T; ++it) {
		scanf("%s\n", &s);
		int n = strlen(s);
		printf("Case #%d: ", it);
		get(0, n);
		puts("");
	}
	return 0;
}