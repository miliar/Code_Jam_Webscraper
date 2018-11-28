#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define uint unsigned int
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

using namespace std;

int n, q, u, v;
int dis[101][101];
int e[101], s[101];
bool flag[101];
double dp[101];

void solve() {
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++)
		cin >> e[i] >> s[i];
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> dis[i][j];
	cin >> u >> v;
	for (int i = 1; i <= n; i++)
		flag[i] = false;
	dp[1] = 0, flag[1] = true;
	for (int i = 1; i < n; i++) {
		int len = 0, node = i;
		while (node < n && e[i] >= dis[node][node + 1]) {
			e[i] -= dis[node][node + 1];
			len += dis[node][node + 1];
			node++;
			if (!flag[node]) {
				dp[node] = dp[i] + len * 1.0 / s[i];
				flag[node] = true;
			} else
				dp[node] = min(dp[node], dp[i] + len * 1.0 / s[i]);
		}
	}
	cout << fixed << setprecision(7) << dp[n] << endl;
}

int main() {
	int t, i;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
