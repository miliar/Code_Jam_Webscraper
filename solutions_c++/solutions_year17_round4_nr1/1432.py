#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int N;
int G[100];
int c[4];
int d[101][101][101];

int solve2() {
	return c[0] + ((c[1] + 1) >> 1);
}
int solve3() {
	if (c[2] < c[1]) swap(c[2], c[1]);
	int d = c[2] - c[1];
	return c[0] + c[1] + (d + 2) / 3;
}
int search(int x, int y, int z) {
	if (x < 0 || y < 0 || z < 0) return -100;
	if (d[x][y][z] >= 0) return d[x][y][z];
	int ret = search(x - 4, y, z);
	int t = search(x - 2, y - 1, z);
	if (t > ret) ret = t;
	t = search(x - 1, y, z - 1);
	if (t > ret) ret = t;
	t = search(x, y - 2, z);
	if (t > ret) ret = t;
	t = search(x, y - 1, z - 2);
	if (t > ret) ret = t;
	t = search(x, y, z - 4);
	if (t > ret) ret = t;
	return d[x][y][z] = ret + 1;
}
int solve4() {
	return c[0] + search(c[1], c[2], c[3]);
}
int main() {
	int T;
	int (*funcptr[3])() = { solve2, solve3, solve4 };
	memset(d, -1, sizeof(d));
	d[0][0][0] = 0;
	d[1][0][0] = d[2][0][0] = d[3][0][0] = 1;
	d[0][0][1] = d[0][0][2] = d[0][0][3] = 1;
	d[0][1][0] = d[1][1][0] = d[0][1][1] = 1;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int P;
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; ++i) scanf("%d", G + i);
		for (int i = 0; i < P; ++i) c[i] = 0;
		for (int i = 0; i < N; ++i) ++c[G[i] % P];
		int ans = funcptr[P - 2]();
		printf("Case #%d: %d\n", t, ans);
	}
}
