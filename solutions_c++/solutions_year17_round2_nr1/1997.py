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
const int N = 1000;
int d, n, at[N], s[N];
double lastH;
pair<int, int> v[N];
bool check(double m) {
	double need = d / m;
	return need >= lastH;
}
int main()
{
	freopen("C:/Users/ASUS/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d:", tt);
		scanf("%d%d", &d, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &v[i].first, &v[i].second);
		sort(v, v + n);
		for (int i = 0; i < n; ++i) {
			at[i] = v[i].first;
			s[i] = v[i].second;
		}
		vector<double> speed(n);
		lastH = 0;
		for (int i = n - 1; i >= 0; --i) {
			double l = 0, r = s[i];
			for (int it = 0; it < 256; ++it) {
				double m = (l + r) / 2;
				bool ok = true;
				for (int j = i + 1; j < n; ++j) {
					if (m <= speed[j] + 1e-9)
						continue;
					double mt = (at[j] - at[i]) / double(m - speed[j]);
					if (at[i]+mt*m < d) {
						ok = false;
						break;
					}
				}
				if (ok)
					l = m;
				else
					r = m;
			}
			speed[i] = l;
			lastH = max(lastH, double(d - at[i]) / speed[i]);
		}
		double l = 0, r = 1e17;
		for (int it = 0; it < 256; ++it) {
			double m = (l + r) / 2;
			if (check(m))
				l = m;
			else
				r = m;
		}
		printf(" %.9lf\n", l);
	}
	return 0;
}