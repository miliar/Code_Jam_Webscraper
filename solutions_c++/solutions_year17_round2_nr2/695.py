#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template <typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0' || ch>'9'; ch = getchar());
	for (; ch<='9' && ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
const int N = 1000, M = 1 << 27;
const char ctbl[] = "RYB";
int f[N + 2][N + 2][N + 2];
int tr[M][3];
int n, a[6];
void pre() {
	for (int t=0; t<M; ++t) {
		for (int i=0; i<3; ++i) {
			#define upd1(i, j, k) if ((t >> (i * 9 + j * 3)) & 7) tr[t][k] |= 1 << (i * 9 + k * 3 + j)
			upd1(i, 0, 1);
			upd1(i, 0, 2);
			upd1(i, 1, 0);
			upd1(i, 1, 2);
			upd1(i, 2, 0);
			upd1(i, 2, 1);
		}
	}
	fprintf(stderr, "pre1\n");
	f[1][0][0] = 7 << (0 * 9 + 0 * 3);
	f[0][1][0] = 7 << (1 * 9 + 1 * 3);
	f[0][0][1] = 7 << (2 * 9 + 2 * 3);
	for (int i=0; i<=N; ++i)
		for (int j=0; i+j<=N; ++j)
			for (int k=0; i+j+k<=N; ++k) {
				f[i + 1][j][k] |= tr[f[i][j][k]][0];
				f[i][j + 1][k] |= tr[f[i][j][k]][1];
				f[i][j][k + 1] |= tr[f[i][j][k]][2];
			}
	fprintf(stderr, "pre2\n");
}
string solve(int a[]) {
	int x = a[0], y = a[1], z = a[2], c;
	if (x > 0) c = 0, ++x; else
	if (y > 0) c = 1, ++y; else
	if (z > 0) c = 2, ++z; else
		return string();
	
	if (!((f[x][y][z] >> (c * 9 + c * 3)) & 7))
		return string("IMPOSSIBLE");
	
	string res = string();
	int cur = c, curf;
	while (x + y + z > 1) {
		curf = f[x][y][z];
		if (cur == 0) --x; else
		if (cur == 1) --y; else
			--z;
		cur = __builtin_ctz(curf >> (c * 9 + cur * 3));
		res += ctbl[cur];
	}
	return res;
}
void run() {
	scanf("%d%d%d%d%d%d%d", &n, a + 0, a + 3, a + 1, a + 4, a + 2, a + 5);
	a[0] -= a[4];
	a[1] -= a[5];
	a[2] -= a[3];
	string r = solve(a);
	puts(r.c_str());
}
int main( ){
	pre();
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}