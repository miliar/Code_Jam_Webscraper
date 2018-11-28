#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iterator>
#include <map>
using namespace std;

typedef long long li;
const li MOD = 1e9 + 7;

const int K = 9;
const int N = 1500;
const int INF = 1e9;
const int M = 800;
li dp[N][N];
li mxdp[N][N];

vector < pair < li, li >> a;
int n, k;
const long double PI = acos(-1.0);


int t[N];
int z[N][2][2][M];

int day = 1440;
int calc(int idx, int p, int f, int need)
{
	if (z[idx][p][f][need] != -1) return z[idx][p][f][need];

	if (idx == day) {
		if (p == f && need == 0) {
			return z[idx][p][f][need] = 0;
		}
		else {
			return z[idx][p][f][need] = INF;
		}
	}
	z[idx][p][f][need] = INF;
	if (p != t[idx] && calc(idx + 1, p, f, need - p) < INF) {
		z[idx][p][f][need] = min(z[idx][p][f][need], calc(idx + 1, p, f, need - p));
	}
	if (1 - p != t[idx] && calc(idx + 1, 1 - p, f, need - (1 - p)) < INF) {
		z[idx][p][f][need] = min(z[idx][p][f][need], 1 + calc(idx + 1, 1 - p, f, need - (1 - p)));
	}
	return z[idx][p][f][need];
}
void solve()
{
	int test;
	cin >> test;
	for (int q = 0; q < test; q++) {
		for (int i = 0; i < N; i++) {
			t[i] = -1;
			for (int p = 0; p < 2; p++) {
				for (int f = 0; f < 2; f++) {
					for (int need = 0; need < M; need++)
						z[i][p][f][need] = -1;
				}
			}
		}
		int ac, at;
		cin >> ac >> at;
		for (int i = 0; i < ac; i++) {
			int c, d;
			cin >> c >> d;
			for (int j = c; j < d; j++) {
				t[j % day] = 0;
			}
		}
		for (int i = 0; i < at; i++) {
			int c, d;
			cin >> c >> d;
			for (int j = c; j < d; j++) {
				t[j % day] = 1;
			}
		}
		int ans = calc(0, 0, 0, day / 2);
		ans = min(ans, calc(0, 1, 1, day / 2));
		cout << "Case #" << q + 1 << ": " << ans << endl;
	}
}

int main() {
	cout << setprecision(15) << fixed;
#if _DEBUG
#endif
	freopen("B-large (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin.tie(0);
	cout.sync_with_stdio(false);
	solve();
	return 0;
}