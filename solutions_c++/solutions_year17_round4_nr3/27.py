#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;
const i64 MOD = 0;
template <typename T> void ADD(T &a, const T b) { a = (a + b) % MOD; }
int T;

int H, W;
char in[55][55];
int sid[55][55];
vector<int> visa[55][55], visb[55][55];

bool shoot(int y, int x, int dy, int dx, int ori)
{
//	printf("%d %d %d %d: \n", y, x, dy, dx);
	for (;;) {
		y += dy;
		x += dx;
		//printf("  %d %d\n", y, x);
		if (y < 0 || x < 0 || y >= H || x >= W) break;

		if (in[y][x] == '#') break;
		if (in[y][x] == '.') {
			if (dy == 0) visa[y][x].push_back(ori);
			else visb[y][x].push_back(ori);
		}
		if (in[y][x] == '-' || in[y][x] == '|') return true;
		if (in[y][x] == '/') {
			swap(dy, dx);
			dy *= -1;
			dx *= -1;
		}
		if (in[y][x] == '\\') {
			swap(dy, dx);
		}
	}
	return false;
}

#define MAXN 10000
// END CUT HERE
/* scc の値が大きい : グラフ上末端に近い．rev には逆グラフを入れる */
int C, N; int scc[MAXN]; ivec graph[MAXN], rev[MAXN], st;
void ae(int p, int q) {
	graph[p].push_back(q);
	rev[q].push_back(p);
//	printf("%d->%d\n", p, q);
}
void visit0(int p) {
	scc[p] = -1;
	for (auto q : graph[p]) if (!scc[q]) visit0(q);
	st.push_back(p);
}
void visit1(int p) {
	scc[p] = C;
	for (auto q : rev[p]) if (!~scc[q]) visit1(q);
}
void scc_go() {
	memset(scc, 0, N * 4); C = 0; st.clear();
	for (int i = 0; i < N; ++i) if (!scc[i]) visit0(i);
	for (int i = N - 1; i >= 0; --i) if (!~scc[st[i]]) ++C, visit1(st[i]);
}

void cond_or(int p, int q) {
//	printf("%d || %d\n", p, q);
	ae(p ^ 1, q);
	ae(q ^ 1, p);
}

vector<int> tgs[10000];
int val[10000];

bool tester()
{
	int fl[50][50];
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) fl[i][j] = 0;
	}
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			if (in[i][j] == '|') {
				for (int i2 = i - 1; i2 >= 0; --i2) {
					if (in[i2][j] == '#') break;
					if (in[i2][j] == '|' || in[i2][j] == '-') {
					//	printf("%d %d\n", i2, j);
						return false;
					}
					fl[i2][j] = 1;
				}
				for (int i2 = i + 1; i2 < H; ++i2) {
					if (in[i2][j] == '#') break;
					if (in[i2][j] == '|' || in[i2][j] == '-') {
					//	printf("%d %d\n", i2, j);
						return false;
					}
					fl[i2][j] = 1;
				}
			} else if (in[i][j] == '-') {
				for (int j2 = j - 1; j2 >= 0; --j2) {
					if (in[i][j2] == '#') break;
					if (in[i][j2] == '|' || in[i][j2] == '-') return false;
					fl[i][j2] = 1;
				}
				for (int j2 = j + 1; j2 < W; ++j2) {
					if (in[i][j2] == '#') break;
					if (in[i][j2] == '|' || in[i][j2] == '-') return false;
					fl[i][j2] = 1;
				}
			}
		}
	}
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			if (in[i][j] == '.' && fl[i][j] == 0) return false;
		}
	}
	return true;
}

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%d%d", &H, &W);
		for (int i = 0; i < H; ++i) {
			scanf("%s", in[i]);
		}
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				visa[i][j].clear();
				visb[i][j].clear();
			}
		}
		for (int i = 0; i < MAXN; ++i) {
			graph[i].clear();
			rev[i].clear();
		}
		int at;
		int i0 = 0;
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (in[i][j] == '-' || in[i][j] == '|') {
					sid[i][j] = i0++;
				} else {
					sid[i][j] = -1;
				}
			}
		}
		// i0: always true
		cond_or(i0 * 2, (i0 + 1) * 2);
		cond_or(i0 * 2, (i0 + 1) * 2 + 1);

		at = i0 * 2;

		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (sid[i][j] == -1) continue;
				int mi = sid[i][j];

				if (shoot(i, j, 1, 0, mi * 2)) {
					cond_or(at ^ 1, mi * 2 + 1);
				}
				if (shoot(i, j, -1, 0, mi * 2)) {
					cond_or(at ^ 1, mi * 2 + 1);
				}
				if (shoot(i, j, 0, 1, mi * 2 + 1)) {
					cond_or(at ^ 1, mi * 2);
				}
				if (shoot(i, j, 0, -1, mi * 2 + 1)) {
					cond_or(at ^ 1, mi * 2);
				}
			}
		}
		bool isok = true;
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (in[i][j] != '.') continue;

				if (visa[i][j].size() == 1 && visb[i][j].size() == 1) {
					cond_or(visa[i][j][0], visb[i][j][0]);
				} else if (visa[i][j].size() == 1) {
					cond_or(at ^ 1, visa[i][j][0]);
				} else if (visb[i][j].size() == 1) {
					cond_or(at ^ 1, visb[i][j][0]);
				} else {
					isok = false;
				}
			}
		}
		N = (i0 + 2) * 2;
		scc_go();

		for (int i = 0; i < i0 + 2; ++i) {
		//	printf("%d %d\n", scc[i * 2], scc[i * 2 + 1]);
			if (scc[i * 2] == scc[i * 2 + 1]) isok = false;
		}

		if (!isok) {
			printf("Case #%d: IMPOSSIBLE\n", t);
			for (int i = 0; i < H; ++i) fprintf(stderr, "%s\n", in[i]);
			continue;
		}
		printf("Case #%d: POSSIBLE\n", t);

		for (int i = 0; i < N; ++i) val[i] = -1;
		for (int i = 0; i < N; ++i) tgs[scc[i]].push_back(i);

		for (int i = 0; i < C; ++i) {
			bool req_true = false;
			for (int p : tgs[i]) {
				if (val[p] == 1) req_true = true;
			}

			if (!req_true) {
				for (int p : tgs[i]) {
					val[p] = 0;
					val[p ^ 1] = 1;
				}
			} else {
				for (int p : tgs[i]) {
					val[p] = 1;
					val[p ^ 1] = 0;
					for (int q : graph[p]) {
						val[q] = 1;
						val[q ^ 1] = 0;
					}
				}
			}
		}
		//for (int i = 0; i < H; ++i) fprintf(stderr, "%s\n", in[i]);
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (sid[i][j] != -1) {
					if (in[i][j] != '|' && in[i][j] != '-') fprintf(stderr, "><");
					if (val[sid[i][j] * 2] == 1) in[i][j] = '|';
					else in[i][j] = '-';
				}
			}
		}
		///for (int i = 0; i < H; ++i) fprintf(stderr, "%s\n", in[i]);
		//fprintf(stderr, "\n");
		if (!tester()) {
			fprintf(stderr, "><><><\n");
		}
		for (int i = 0; i < H; ++i) puts(in[i]);
		for (int i = 0; i < 10000; ++i) tgs[i].clear();
	}

	return 0;
}
