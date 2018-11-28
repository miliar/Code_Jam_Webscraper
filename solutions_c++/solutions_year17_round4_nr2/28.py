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

int rup(int p, int q)
{
	return p / q + (p % q != 0 ? 1 : 0);
}

int N, C, M;
int P[1010], B[1010];
int cnt[1010][1010];

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%d%d%d", &N, &C, &M);
		for (int i = 0; i < M; ++i) {
			scanf("%d%d", P + i, B + i);
			--P[i]; --B[i];
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < C; ++j) {
				cnt[i][j] = 0;
			}
		}
		for (int i = 0; i < M; ++i) {
			++cnt[P[i]][B[i]];
		}
		int x = 0;

		int rs[1010];
		for (int i = 0; i < N; ++i) {
			int w = 0;
			for (int j = 0; j < C; ++j) w += cnt[i][j];
			rs[i] = w;
		}
		int sum = 0;
		for (int i = 0; i < N; ++i) {
			sum += rs[i];
			x = max(x, rup(sum, i + 1));
		}
		for (int j = 0; j < C; ++j) {
			int w = 0;
			for (int i = 0; i < N; ++i) w += cnt[i][j];
			x = max(x, w);
		}
		int y = 0;
		for (int i = 0; i < N; ++i) y += max(0, rs[i] - x);

		printf("Case #%d: %d %d\n", t, x, y);
	}

	return 0;
}
