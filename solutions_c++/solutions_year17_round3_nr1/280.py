#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <iostream>

using namespace std;

const int maxn = 1010;
const double pi = acos(-1.0);

int T, n, k, rnk[maxn];
double r[maxn], h[maxn], a[maxn], res, sa, mr;

int cmp(int i, int j) {
	return a[i] > a[j];
}

int main() {
	freopen("A-large.in.txt", "r", stdin);
	freopen("ans.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> n >> k;
		for(int i = 0; i < n; i ++) {
			cin >> r[i] >> h[i];
			a[i] = 2*r[i]*h[i];
			rnk[i] = i;
		}
		sort(rnk, rnk+n,cmp);
		
		res = sa = mr = 0;
		for(int j = 0; j < k-1; j ++) {
			int i = rnk[j];
			sa += a[i];
			mr = max(mr, r[i]);
		}
		for(int j = k-1; j < n; j ++) {
			int i = rnk[j];
			double _r = mr;
			if(r[i] > mr) _r = r[i];
			res = max(res, sa+a[i] + _r*_r);
		}
		printf("Case #%d: %.9f\n", cas, res*pi);
	}
	return 0;
}

