#include <cstdio>
#include <vector>
#include <string.h>
#include <math.h>
#define feq(x,y) (fabs((x)-(y))<eps)
#define flt(x,y) ((x)<(y)-eps)
#define fgt(x,y) ((x)>(y)+eps)
#define fle(x,y) ((x)<(y)+eps)
#define fge(x,y) ((x)>(y)-eps)
const double inf = 1e40, eps = 1e-9;

using namespace std;

struct r {
	int x, y, p, l;
	bool d;
	r() {}
	r(int x, int y): x(x), y(y) { d = false;}
	r(int x, int y, int p, int l): x(x), y(y), p(p), l(l) {}
	bool operator<(const r &a) const {
		return x < a.x;
	}
};

int mymax(int a, int b, int c) {
	return max(a, max(b, c));
}

int solve() {
	int n[2];
	scanf("%d%d", &n[0], &n[1]);
	vector< r> b; b.clear();
	vector< r > a[2];
	for (int j = 0; j < 2; j++) {
		a[j].clear();
		for (int i = 0; i < n[j]; i++) {
			int x, y;
			scanf("%d%d", &x, &y);
			a[j].push_back(r(x, y));
		}
		sort(a[j].begin(), a[j].end());
	}


	for (int j = 0; j < 2; j++) {
		for (int i = 0; i < n[j]; i++) {
			b.push_back(r(a[j][i].x, a[j][i].y, j, i));
		}
	}
	sort(b.begin(), b.end());

	int m = b.size();
	for (int i = 1; i < m; i++) {
		if (b[i].p != b[i - 1].p) {
			int p = b[i - 1].p;
			int l = b[i - 1].l;
			a[p][l].d = true;
		}
	}
	a[b[m - 1].p][b[m - 1].l].d = true;

	for (int j = 0; j < 2; j++) {
		if (n[j] == 0) continue;
		int ts = a[j][0].x;
		int tt = a[j][0].y;
		for (int i = 1; i < n[j]; i++) {
			if (a[j][i].y - ts > 720 && tt + 1440 - a[j][i].x > 720) {
				a[j][i - 1].d = true;
				ts = a[j][i].x;
				tt = a[j][i].y;
			}
			if (a[j][i].d) {
				ts = -1;
				tt = -1;
			} else if (ts == -1) {
				ts = a[j][i].x;
				tt = a[j][i].y;
			}
		}
	}

	int c = 0;
	for (int j = 0; j < 2; j++) {
		for (int i = 0; i < n[j]; i++) {
			// printf("%d %d %d %d\n", j, a[j][i].x, a[j][i].y, a[j][i].d);
			if (a[j][i].d) {
				c++;
			}
		}
	}

	if ((n[0] == 0 || n[1] == 0)) return c * 2;
	return c;
}

int main() {
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		// printf("----------------------------------------------------\n");
		int ans = solve();
		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}
