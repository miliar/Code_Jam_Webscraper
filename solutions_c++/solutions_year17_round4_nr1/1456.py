#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <functional>

using namespace std;
#define lli long long int
const int N = 101;
const lli INF = (lli)1e16;
const lli M = (int)(1e9 + 7);

int a[N][N][N][N][4];
int cnt[4];

int solve(vector<int> v, int p) {
	vector<int> a(v.size());
	for (int i = 0; i < a.size(); ++i) a[i] = i;
	int ans = 0;
	do {
		int fr = 0, la = 0;
		for (int i = 0; i < a.size(); ++i) {
			int val = v[a[i]];
			if (val % p == 0) {
				continue;

			}
			if (val % p <= fr) fr -= val % p;
			else {
				la++;

			}
		}
		ans = max(ans, la);
	} while (next_permutation(a.begin(), a.end()));
}

int main() {
	ios_base::sync_with_stdio();

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		int n, p;
		cin >> n >> p;
		memset(cnt, 0, 4 * sizeof(int));
		for (int i = 0; i < n; ++i) {
			int t;
			cin >> t;
			cnt[t % p]++;
		}
		int ans = cnt[0];
		memset(a, -1, N*N*N*N*4*sizeof(int));
		a[0][0][0][0][0] = 0;
		n = cnt[1] + cnt[2] + cnt[3];
		for (int i = 0; i < n; ++i) {
			for (int c1 = 0; c1 <= cnt[1]; ++c1) {
				for (int c2 = 0; c2 <= cnt[2]; ++c2) {
					for (int c3 = 0; c3 <= cnt[3]; ++c3) {
						for (int fr = 0; fr < p; ++fr) {
							if (a[i][c1][c2][c3][fr] == -1) continue;
							if (c1 < cnt[1]) {
								if (fr > 0) {
									a[i + 1][c1 + 1][c2][c3][fr - 1] = max(a[i + 1][c1 + 1][c2][c3][fr - 1], a[i][c1][c2][c3][fr]);
								}
								else {
									a[i + 1][c1 + 1][c2][c3][fr + p - 1] = max(a[i + 1][c1 + 1][c2][c3][fr + p - 1], (fr == 0) + a[i][c1][c2][c3][fr]);
								}
							}
							if (p > 2 && c2 < cnt[2]) {
								if (fr > 1) {
									a[i + 1][c1][c2 + 1][c3][fr - 2] = max(a[i + 1][c1][c2 + 1][c3][fr - 2], a[i][c1][c2][c3][fr]);
								}
								else {
									a[i + 1][c1][c2 + 1][c3][fr + p - 2] = max(a[i + 1][c1][c2 + 1][c3][fr + p - 2], (fr == 0) + a[i][c1][c2][c3][fr]);
								}
							}
							if (p > 3 && c3 < cnt[3]) {
								if (fr > 2)
									a[i + 1][c1][c2][c3 + 1][fr - 3] = max(a[i + 1][c1][c2][c3 + 1][fr - 3], a[i][c1][c2][c3][fr]);
								else
									a[i + 1][c1][c2][c3 + 1][fr + p - 3] = max(a[i + 1][c1][c2][c3 + 1][fr + p - 3], (fr == 0) + a[i][c1][c2][c3][fr]);
							}
						}
					}
				}
			}
		}
		int la = max(a[n][cnt[1]][cnt[2]][cnt[3]][0], a[n][cnt[1]][cnt[2]][cnt[3]][1]);
		la = max(la, a[n][cnt[1]][cnt[2]][cnt[3]][2]);
		la = max(la, a[n][cnt[1]][cnt[2]][cnt[3]][3]);

		cout << la + ans;

		cout << endl;

		cerr << qq << endl;
	}
	return 0;
}
