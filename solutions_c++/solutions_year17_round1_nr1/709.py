#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

#define NN 32
int t, NY, NX;

struct P {
	int x;
	int y;
};

struct R {
	int x0;
	int x1;
	int y0;
	int y1;
};

P Q[NN*NN];
int qp;
unordered_set<int> chars;
R rects[128];
char F[NN][NN];

bool intersects(const R& r, const R& p)
{
	return !(r.x1 < p.x0 || p.x1 < r.x0 || r.y1 < p.y0 || p.y1 < r.y0);
}

void extends(R& r, int y, int x)
{
	r.x0 = min(x, r.x0);
	r.x1 = max(x, r.x1);
	r.y0 = min(y, r.y0);
	r.y1 = max(y, r.y1);
}
	
bool set(int y, int x, int c)
{
	auto r = rects[c];
	extends(r, y, x);
	for (int c2 : chars) {
		if (c == c2) {
			continue;
		}
		if (intersects(r, rects[c2])) {
			return false;
		}
	}
	rects[c] = r;
	return true;
}

bool solve(int qr)
{
	if (qr == qp) {
		return true;
	}
	for (int c : chars) {
		R r = rects[c];
		if (set(Q[qr].y, Q[qr].x, c)) {
			if (solve(qr + 1)) {
				return true;
			}
			rects[c] = r;
		}
	}
	return false;
}

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d%d", &NY, &NX);
		qp = 0;
		chars.clear();
		memset(rects, 0, sizeof(rects));
		for (int y = 0; y < NY; ++y) {
			char s[NN];
			scanf("%s", s);
			for (int x = 0; x < NX; ++x) {
				int c = s[x];
				if (c == '?') {
					Q[qp].x = x;
					Q[qp].y = y;
					++qp;
				} else if (chars.insert(c).second) {
					rects[c].x0 = x;
					rects[c].x1 = x;
					rects[c].y0 = y;
					rects[c].y1 = y;
				} else {
					extends(rects[c], y, x);
				}
			}
		}
		solve(0);
		memset(F, '\0', sizeof(F));
		for (int c : chars) {
			for (int y = rects[c].y0; y <= rects[c].y1; ++y) {
				for (int x = rects[c].x0; x <= rects[c].x1; ++x) {
					F[y][x] = c;
				}
			}
		}
		printf("Case #%d:\n", ti+1);
		for (int y = 0; y < NY; ++y) {
			printf("%s\n", F[y]);
		}
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
