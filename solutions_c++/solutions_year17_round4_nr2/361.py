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

const int N = 1000 + 1;

int a[N][N];
int cnt[N];
int n, c, m;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		memset(a, 0, sizeof a);
		memset(cnt, 0, sizeof cnt);
		int ret = 0;

		scanf("%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; ++i) {
			int p, b;
			scanf("%d%d", &p, &b);
			++a[--b][--p];
		}

		for (int i = 0; i < c; ++i) {
			int tmp = 0;
			for (int j = 0; j < n; ++j) {
				tmp += a[i][j];
			}
			ret = max(ret, tmp);
		}

		int tmp = 0;
		for (int j = 0; j < n; ++j) {
			for (int i = 0; i < c; ++i) {
				tmp += a[i][j];
			}
			ret = max(ret, (tmp + j) / (j + 1));
		}

		for (int j = 0; j < n; ++j) {
			for (int i = 0; i < c; ++i) {
				cnt[j] += a[i][j];
			}
		}

		int ret2 = 0;
		for (int j = n - 1; j >= 0; --j) {
			for (cnt[j] -= ret; cnt[j] > 0; --cnt[j]) {
				for (int i = j - 1; i >= 0; --i) {
					if (cnt[i] < ret) {
						++cnt[i];
						break;
					}
				}
				++ret2;
			}
		}

		printf("Case #%d: %d %d\n", _, ret, ret2);
	}
	return 0;
}
