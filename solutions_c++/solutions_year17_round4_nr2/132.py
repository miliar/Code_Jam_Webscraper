/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>

#define ll long long
#define ld double
#define pii pair <int, int>
#define pll pair <ll, ll>
#define mp make_pair

using namespace std;

const int maxn = 1010;

int cnt[maxn];
int num[maxn];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	for (int itt = 1; itt <= t; itt++) {
		printf("Case #%d: ", itt);

		int n, c, m;

		cin >> n >> c >> m;

		memset(cnt, 0, sizeof cnt);
		memset(num, 0, sizeof num);

		for (int i = 0; i < m; i++) {
			int p, b;

			scanf("%d %d", &p, &b);

			cnt[p]++;
			num[b]++;
		}

		int ans = 0;

		for (int i = 1; i <= m; i++) {
			ans = max(ans, num[i]);
		}

		int sum = 0;

		for (int i = 1; i <= n; i++) {
			sum += cnt[i];

			ans = max(ans, (sum + i - 1) / i);
		}

		printf("%d ", ans);

		int res = 0;

		for (int i = 1; i <= n; i++) {
			res += max(0, cnt[i] - ans);
		}

		printf("%d\n", res);
	}

	return 0;
}
