#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <stdio.h>
#include <set>
#include <algorithm>
#include <string.h>
#include <sstream>
#include <assert.h>
#include <time.h>
#include <string>
#include <queue>
#include <random> 
#include <map>
#include <numeric>
using namespace std;
typedef long long li;
#define mp make_pair
#define sz(a) (int)a.size()
const int N = 1e5 + 5;
const int K = 1e4 + 5;
const int INF = 1e9 + 7;
int a[N];

void solve() {
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		int n, p;
		cin >> n >> p;
		vector<int> a(n);
		vector<int> cnt(5, 0);
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			a[i] %= p;
			cnt[a[i]]++;
		}
		int ans = 0;

		if (p == 2) {
			ans = cnt[0] + (cnt[1] + 1) / 2;
		}
		if (p == 3) {
			ans = cnt[0];
			int cn = min(cnt[1], cnt[2]);
			cnt[1] -= cn;
			cnt[2] -= cn;
			ans += cn;

			for (int j = 1; j <= 2; j++) {
				int sum = 0;
				for (int i = 0; i < cnt[j]; i++) {
					if (sum % p == 0) {
						ans++;
					}
					sum += j;
				}
			}
		}

		if (p == 4) {
			ans = cnt[0];
			int cn = min(cnt[1], cnt[3]);
			cnt[1] -= cn;
			cnt[3] -= cn;
			ans += cn;

			int cn2 = cnt[2] / 2;
			cnt[2] -= 2 * cn2;
			ans += cn2;

			int ans1 = 0, ans2 = 0;
			{
				int sum = 0;
				for (int i = 0; i < cnt[1]; i++) {
					if (sum % p == 0) {
						ans1++;
					}
					sum += 1;
				}
				for (int i = 0; i < cnt[3]; i++) {
					if (sum % p == 0) {
						ans1++;
					}
					sum += 3;
				}
				for (int i = 0; i < cnt[2]; i++) {
					if (sum % p == 0) {
						ans1++;
					}
					sum += 2;
				}
			}

			{
				int sum = 0;
				for (int i = 0; i < cnt[2]; i++) {
					if (sum % p == 0) {
						ans2++;
					}
					sum += 2;
				}
				for (int i = 0; i < cnt[1]; i++) {
					if (sum % p == 0) {
						ans2++;
					}
					sum += 1;
				}
				for (int i = 0; i < cnt[3]; i++) {
					if (sum % p == 0) {
						ans2++;
					}
					sum += 3;
				}
			}


			ans += max(ans1, ans2);
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
}

int main() {
#ifdef _DEBUG
	freopen("A-large (4).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cout.sync_with_stdio(false);
	cin.tie(0);
	srand(time(NULL));
	solve();
	return 0;
}