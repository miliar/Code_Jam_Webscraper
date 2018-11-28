#include <cstdio>
#include <cassert>

#define iter(i, n) for (int i = 1; i <= n; ++i)
#define NR 310

int T, n, m, N;
bool g0[NR][NR], g1[NR][NR], vx[NR], vy[NR], va[NR], vb[NR], v0[NR], v1[NR];
int my[NR], mb[NR];
char s[NR][NR];

void add0(int x, int y) {
	vx[x] = vy[y] = true;
	my[y] = x;
}

void add1(int x, int y) {
	va[x - y + n] = vb[x + y - 1] = true;
	mb[x + y - 1] = x - y + n;
}

bool dfs0(int x) {
	iter(y, n) if (!v0[y] && g0[x][y]) {
		v0[y] = true;
		if (my[y] == -1 || dfs0(my[y])) return my[y] = x, true;
	}
	return false;
}

bool dfs1(int x) {
	iter(y, N) if (!v1[y] && g1[x][y]) {
		v1[y] = true;
		if (mb[y] == -1 || dfs1(mb[y])) return mb[y] = x, true;
	}
	return false;
}

void match0() {
	iter(i, n) {
		iter(j, n) v0[j] = false;
		dfs0(i);
	}
}

void match1() {
	iter(i, N) {
		iter(j, N) v1[j] = false;
		dfs1(i);
	}
}

int main() {
	freopen("D.in", "r", stdin);
	scanf("%d", &T);

	for (int id = 1; id <= T; ++id) {
		scanf("%d%d", &n, &m);
		N = 2 * n - 1;

		iter(i, n) vx[i] = vy[i] = false, my[i] = -1;
		iter(i, N) va[i] = vb[i] = false, mb[i] = -1;
		iter(i, n) iter(j, n) s[i][j] = '.';

		iter(i, m) {
			int x, y; char ch[10];
			scanf("%s%d%d", ch, &x, &y);
			s[x][y] = ch[0];
			if (ch[0] == 'o') add0(x, y), add1(x, y);
			else if (ch[0] == '+') add1(x, y);
			else add0(x, y);
		}

		iter(i, n) iter(j, n) g0[i][j] = (!vx[i] && !vy[j]);
		iter(i, N) iter(j, N) g1[i][j] = false;

		iter(i, n) iter(j, n) {
			int x = i - j + n, y = i + j - 1;
			g1[x][y] = (!va[x] && !vb[y]);
		}

		match0();
		match1();

		int ans = 0, cnt = 0;

		iter(i, n) iter(j, n) {

			bool a = (my[j] == i), b = (mb[i + j - 1] == i - j + n);
			ans += a + b;
			if (s[i][j] != 'o' && a && b) ++cnt;
			else if (s[i][j] == '.') { if (a || b) ++cnt; }
		}
		printf("Case #%d: %d %d\n", id, ans, cnt);
		iter(i, n) iter(j, n) {
			bool a = (my[j] == i), b = (mb[i + j - 1] == i - j + n);
			if (s[i][j] != 'o' && a && b) printf("o %d %d\n", i, j);
			else if (s[i][j] == '.') { if (a || b) printf("%c %d %d\n", a ? 'x' : '+', i, j); }
			else if (s[i][j] != 'o') {
				if (s[i][j] == '+') assert(b && !a);
				else if (!(!b && a)) fprintf(stderr, "!!%d %d %d\n", id, i, j);
			}
		}
	}
	return 0;
}