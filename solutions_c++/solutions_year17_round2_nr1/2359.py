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
const ll INF = static_cast<ll>(1e18);

int x[1009];
int s[1009];

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int test_number = 1; test_number <= t; ++test_number) {
		int d, n;
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d", &x[i], &s[i]);
		}
		double l = 0;
		double r = INF;
		for (int iteration_number = 0; iteration_number < 100; ++iteration_number) {
			double m = (l + r) / 2.0;
			bool is_valid = true;
			double time_needed = d / m;
			for (int i = 0; i < n; ++i) {
				if (x[i] + time_needed * s[i] < d) {
					is_valid = false;
					break;
				}
			}
			if (is_valid) {
				l = m;
			} else {
				r = m;
			}
		}
		printf("Case #%d: %.12lf\n", test_number, l);
	}
	return 0;
}