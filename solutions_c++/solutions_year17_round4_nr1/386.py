#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

const int N = 101;

int a[N];
int cnt[4];
int f[4][N][N][N];
int n, p;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		memset(cnt, 0, sizeof cnt);
		memset(f, -1, sizeof f);
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			++cnt[a[i] % p];
		}
		f[0][cnt[1]][cnt[2]][cnt[3]] = 0;
		for (int i = cnt[1]; i >= 0; --i) {
			for (int j = cnt[2]; j >= 0; --j) {
				for (int k = cnt[3]; k >= 0; --k) {
					for (int r = 0; r < p; ++r) {
						if (f[r][i][j][k] == -1) {
							continue;
						}
						if (i > 0) {
							int nr = (r + 1) % p;
							f[nr][i - 1][j][k] = max(f[nr][i - 1][j][k], f[r][i][j][k] + (r == 0));
						}
						if (j > 0) {
							int nr = (r + 2) % p;
							f[nr][i][j - 1][k] = max(f[nr][i][j - 1][k], f[r][i][j][k] + (r == 0));
						}
						if (k > 0) {
							int nr = (r + 3) % p;
							f[nr][i][j][k - 1] = max(f[nr][i][j][k - 1], f[r][i][j][k] + (r == 0));
						}
					}
				}
			}
		}
		int ret = 0;
		for (int r = 0; r < p; ++r) {
			ret = max(ret, f[r][0][0][0]);
		}
		ret += cnt[0];
		printf("Case #%d: %d\n", _, ret);
	}
	return 0;
}
