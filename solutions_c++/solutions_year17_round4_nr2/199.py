#include <stdio.h>
#include <iostream>
#include <vector>
#include <assert.h>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <memory.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, c, t;
vector<pair<int, int> > v;
int check(int r) {
	int ret = 0;
	int emp = 0;
	vector<int> f(n);
	for (int i = 0; i < v.size(); ++i)
		++f[v[i].first];
	for (int i = 0; i < n; ++i) {
		int rem = max(0, f[i] - r);
		if (rem > emp)
			return -1;
		ret += rem;
		emp -= rem;
		emp += max(0, r - f[i]);
	}
	return ret;
}
int main()
{
	//freopen("src.txt", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d:", tt);
		scanf("%d%d%d", &n, &c, &t);
		v.resize(t);
		vector<int> fr(c);
		int mx = 0;
		for (int i = 0; i < t; ++i) {
			scanf("%d%d", &v[i].first, &v[i].second);
			--v[i].first;
			--v[i].second;
			mx = max(mx, ++fr[v[i].second]);
		}
		sort(v.begin(), v.end());
		int l = mx, r = t - 1, m, res = t, pr = 0;
		while (l <= r) {
			m = (l + r) / 2;
			int x = check(m);
			if (x != -1) {
				res = m;
				pr = x;
				r = m - 1;
			}else
				l = m + 1;
		}
		printf(" %d %d\n", res, pr);
	}
	return 0;
}