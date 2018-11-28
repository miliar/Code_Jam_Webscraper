#pragma comment(linker, "/STACK:500000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <exception>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = static_cast<int>(2e9);

bool used[1009];

void getDists(int s, int& l, int& r) {
	l = 0;
	for (int i = s - 1; !used[i]; --i) {
		++l;
	}
	r = 0;
	for (int i = s + 1; !used[i]; ++i) {
		++r;
	}
}

int main() {
	freopen("1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n, k;
		scanf("%d %d", &n, &k);
		used[0] = used[n + 1] = true;
		for (int i = 1; i <= n; ++i) {
			used[i] = false;
		}
		int sAns, lAns, rAns;
		while (k--) {
			sAns = -1;
			for (int s = 1; s <= n; ++s) {
				if (!used[s]) {
					int l, r;
					getDists(s, l, r);
					if (sAns == -1 ||
						min(l, r) > min(lAns, rAns) ||
						(min(l, r) == min(lAns, rAns) && max(l, r) > max(lAns, rAns))) {
						sAns = s;
						lAns = l;
						rAns = r;
					}
				}
			}
			used[sAns] = true;
		}
		printf("Case #%d: %d %d\n", tt, max(lAns, rAns), min(lAns, rAns));
	}
	return 0;
}