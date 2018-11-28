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

char s[1009];

void flip(int l, int r) {
	for (int i = l; i <= r; ++i) {
		if (s[i] == '+') {
			s[i] = '-';
		} else {
			s[i] = '+';
		}
	}
}

int main() {
	freopen("1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int k;
		scanf("%s %d", s, &k);
		int n = strlen(s);
		int res = 0;
		for (int i = 0; i < n; ++i) {
			if (s[i] == '-') {
				if (i + k - 1 >= n) {
					res = INF;
					break;
				}
				++res;
				flip(i, i + k - 1);
			}
		}
		if (res == INF) {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		} else {
			printf("Case #%d: %d\n", tt, res);
		}
	}
	return 0;
}