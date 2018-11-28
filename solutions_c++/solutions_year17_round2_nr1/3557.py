#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <stdio.h>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>
#include <cstring>
using namespace std;

#define MAXN 100001
#define MOD 1000000007
#define INFY 1000000000
#define ESILON 1e-6

struct E
{
	long double k, s, t;
	bool operator < (const E &t) const { return k<t.k; }
};

int n;
long double d;
E h[MAXN];

void Solver() {
	cin >> d >> n;
	for (int i = 0; i < n; i++) {
		cin >> h[i].k >> h[i].s;
	}
	sort(h, h + n);
	for (int i = 0; i < n-1; i++) {
		if (h[i].s > h[i + 1].s) {
			h[i].t = (h[i + 1].k - h[i].k) / (h[i].s - h[i+1].s);
		}
		else {
			h[i].t = -1;
		}
	}
	h[n - 1].t = -1;
	long double l = 1.0, r = 1e18, m, t;
	int run = 0;
	while (r-l > ESILON) {
		m = (r + l) / 2.0;
		t = d / m;
		bool hasCatch = 0;
		for (int i = 0; i < n; i++) {
			long double x;
			if (h[i].t == -1 || t <= h[i].t) {
				x = h[i].k + t * h[i].s;
			}
			else {
				x = h[i].k + h[i].t * h[i].s + (t - h[i].t) * h[i+1].s;
			}
			if (x < d) {
				hasCatch = 1;
				break;
			}
		}
		if (hasCatch) {
			r = m;
		}
		else {
			l = m;
		}
		run++;
		if (run > 100000000) break;
	}
	printf(" %.6lf", m);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int numcase;
	cin >> numcase;

	for (int t = 1; t <= numcase; t++) {
		printf("Case #%d:", t);
		Solver();
		printf("\n");
	}
	return 0;
}