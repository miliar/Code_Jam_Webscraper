#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define N 111

int T, n, p;
int a[N];

int calc() {
	int ans = 0, p1 = 0, p2 = 0;
	if (p == 2) {
		rep(i, n) if (a[i] == 0) ans += 1;
		else p1 += 1;
		ans += (p1+1) / 2;
	}else if (p == 3) {
		rep(i, n) if (a[i] == 0) ans += 1;
		else if (a[i] == 1) p1 += 1; else p2 += 1;
		if (p1 <= p2) {
			ans += p1 + (p2-p1+2)/3;
		} else {
			ans += p2 + (p1-p2+2)/3;
		}
	}
	return ans;
}

void solve() {
	scanf("%d%d", &n, &p);
	rep(i, n) scanf("%d", &a[i]);
	rep(i, n) a[i] %= p;
	printf("%d\n", calc());
}

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	//freopen("a.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}