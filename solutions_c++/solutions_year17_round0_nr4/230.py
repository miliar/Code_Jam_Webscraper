#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cassert>
using namespace std;

int t;
int n, m;

const int NN = 128;
char f0[NN][NN];
char f1[NN][NN];
vector<int> vr, vc, vd1, vd2, mt, used;

bool try_kuhn(int d1)
{
	if (!used[d1]) {
		used[d1] = 1;
		int d2mn = max(d1 - (n - 1), (n - 1) - d1);
		int d2mx = min(3 * (n - 1) - d1, (n - 1) + d1);
		//printf("d1:%d d2mn:%d d2mx:%d\n", d1, d2mn, d2mx);
		for (int d2 = d2mn; d2 <= d2mx; d2 += 2) {
			if (vd2[d2] == 0) {
				if (mt[d2] == -1 || try_kuhn(mt[d2])) {
					mt[d2] = d1;
					return true;
				}
			}
		}
	}
	return false;
}

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d%d", &n, &m);
		vr.assign(n, 0);
		vc.assign(n, 0);
		vd1.assign(2 * n - 1, 0);
		vd2.assign(2 * n - 1, 0);
		memset(f0, '.', sizeof(f0));
		int points = 0;
		for (int i = 0; i < m; ++i) {
			char ch[10];
			int r, c;
			scanf("%s%d%d", ch, &r, &c);
			--r;
			--c;
			f0[r][c] = ch[0];
			if (ch[0] == 'x' || ch[0] == 'o') {
				++vr[r];
				++vc[c];
			}
			if (ch[0] == '+' || ch[0] == 'o') {
				++vd1[r + c];
				++vd2[r + (n - 1) - c];
			}
			if (ch[0] == '+' || ch[0] == 'x') {
				++points;
			} else if (ch[0] == 'o') {
				points += 2;
			}
		}
		memcpy(f1, f0, sizeof(f1));
		int c = 0;
		for (int r = 0; r < n; ++r) {
			if (!vr[r]) {
				while (vc[c]) {
					++c;
				}
				if (f1[r][c] == '+') {
					f1[r][c] = 'o';
				} else {
					f1[r][c] = 'x';
				}
				++points;
				++c;
			}
		}
		// now we should find maximum match in biparate graph vd1<->vd2
		mt.assign(2 * n - 1, -1);
		for (int d1 = 0; d1 < 2 * n - 1; ++d1) {
			used = vd1;
			try_kuhn(d1);
		}
		for (int d2 = 0; d2 < 2 * n - 1; ++d2) {
			int d1 = mt[d2];
			if (d1 != -1) {
				int r = (d1 + d2 - (n - 1)) / 2;
				int c = d1 - r;
				if (f1[r][c] == 'x') {
					f1[r][c] = 'o';
				} else {
					f1[r][c] = '+';
				}
				++points;
			}
		}
		int moves = 0;
		for (int r = 0; r < n; ++r) {
			for (int c = 0; c < n; ++c) {
				if (f1[r][c] != f0[r][c]) {
					++moves;
				}
			}
		}
		printf("Case #%d: %d %d\n", ti+1, points, moves);
		for (int r = 0; r < n; ++r) {
			for (int c = 0; c < n; ++c) {
				if (f1[r][c] != f0[r][c]) {
					printf("%c %d %d\n", f1[r][c], r + 1, c + 1);
				}
			}
		}
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
