#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define xx first
#define yy second
#define N 1111

int T, n, c, tm, m, p, r, mm;
pair<int, int> a[N], b[N], aa[N];
bool u[N];
bool pp[N];
set<int> rc;
int cc[N];

void solve() {
	p = 0;
	r = 0;
	scanf("%d%d%d", &n, &c, &m);
	rep(i, m) scanf("%d%d", &aa[i].xx, &aa[i].yy);
	rep(i, m) a[i] = aa[i];
	mm = m;
	sort(a, a+m);
	while (m) {
		++r;
		tm = 0;
		memset(u, 0, sizeof(u));
		memset(pp, 0, sizeof(pp));
		rc.clear();
		kep(i, n) rc.insert(i);
		for (int i = 0; i < m; i++) {
			if (u[a[i].yy] || rc.empty() || rc.lower_bound(a[i].xx+1) == rc.begin()) {
				b[tm++] = a[i];
				continue;
			}
			int tt = *(--rc.lower_bound(a[i].xx+1));
			u[a[i].yy] = true;
			rc.erase(tt);
			if (tt < a[i].xx)
				if (!pp[a[i].xx]) {
					++p;
					pp[tt] = true;
					//true implies promote to this place
				} else {
					pp[a[i].xx] = false;
					pp[tt] = true;
				}
			else {}
		}
		rep(i, tm) a[i] = b[i];
		m = tm;
	}
	m = mm;
	rep(i, m) a[i] = aa[i];
	p = 0;
	sort(a, a + m);
	memset(cc, 0, sizeof(cc));
	
	for (int i = 0; i < m; i++) {
		if (cc[a[i].xx] < r) cc[a[i].xx] += 1;
		else ++p;
	}


	printf("%d %d\n", r, p);
}

int main() {
	freopen("B-small-attempt3.in", "r", stdin);
	//freopen("b.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}