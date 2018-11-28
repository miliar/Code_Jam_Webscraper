#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef long long ll;
char s[32], res[32];
bool vis[32][2][10];
bool calc(int i, bool l, int last) {
	if (!s[i]) {
		res[i] = 0;
		return true;
	}
	if (vis[i][l][last])
		return false;
	vis[i][l][last] = true;
	for (int d = 9; d >= last; --d) {
		if (s[i] - '0' >= d || l) {
			if (calc(i + 1, l || d < s[i] - '0', d)) {
				res[i] = d + '0';
				return true;
			}
		}
	}
	return false;
}
int main() {
	freopen("C:/Users/ASUS/Downloads/B-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d:", T);
		memset(vis, 0, sizeof(vis));
		scanf("%s", s);
		calc(0, false, 0);
		ll num;
		sscanf(res, "%lld", &num);
		printf(" %lld\n", num);
	}
	return 0;
}