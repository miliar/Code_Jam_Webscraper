#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
using namespace std;
typedef long long lint;

void solve(int tst) {	
	lint D, N;	
	double ans = 1e30;
	cin >> D >> N;
	for (int i = 0; i < N; ++i) {
		lint k, s;
		cin >> k >> s;
		double cur = D * s * 1.0 / (D - k);
		ans = min(ans, cur);
	}
	
	printf("Case #%d: %0.6lf\n", tst, ans);	
}

int main() {
	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}
