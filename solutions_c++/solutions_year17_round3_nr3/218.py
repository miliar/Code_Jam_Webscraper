#include <iostream>
#include <stdio.h>
#include <string>
#include <memory.h>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <time.h>
#include <assert.h>
#include <cmath>
#include <stack>
#include <string.h>
#include <sstream>
#include <algorithm>
using namespace std;
typedef long long ll;
const int N = 50;
int n, k;
double p[N];
int main()
{
	//freopen("src.txt", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/C-small-1-attempt0.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/C-small-1-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d:", T);
		scanf("%d%d", &n, &k);
		double u;
		scanf("%lf", &u);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &p[i]);
		sort(p, p + n);
		double l = 0, r = 1, m;
		for (int it = 0; it < 128; ++it) {
			m = (l + r) / 2;
			double need = 0;
			for (int i = 0; i < n; ++i)
				need += max(0.0, m - p[i]);
			if (need > u)
				r = m;
			else
				l = m;
		}
		double res = 1;
		for (int i = 0; i < n; ++i) {
			p[i] = max(p[i], m);
			res *= p[i];
		}
		printf(" %.9lf\n", res);
	}
	return 0;
}