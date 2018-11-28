#include <bits/stdc++.h>
using namespace std;
const int maxn = 1005;
int k[maxn], s[maxn];
int d, n;
bool judge(double x) {
	double tot = (double)d / x; 
	for(int i = 1; i <= n; i++) {
		if(x > s[i]) {
			if((double)k[i] / (x - s[i]) < tot) return false;
		}
	}
	return true;
}
void solve_small(int cases) {
	scanf("%d%d", &d, &n);
	for(int i = 1; i <= n; i++) {
		scanf("%d%d", &k[i], &s[i]);
	}
	double l = 1, r = 1e15, ans = 0;
	for(int i = 0; i < 100; i++) {
		double mid = (l + r) / 2;
		if(judge(mid)) {
			ans = mid;
			l = mid;
		} else {
			r = mid;
		}
	}
	printf("Case #%d: %.10f\n", cases, ans);
}

void solve_big(int cases) {


}

int main() {
//	freopen("sample_in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.ou", "w", stdout);

	int T, cases = 0;
	
	scanf("%d", &T);
	while(T--) {
		solve_small(++cases);
		//solve_big(++cases);
	}
	return 0;
}
