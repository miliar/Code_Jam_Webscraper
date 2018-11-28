#include<bits/stdc++.h>
using namespace std;
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(0); qq < tests; qq++) {
		int d, n;
		cin >> d >> n;
		double ans(0);
		for(int i(0); i < n; i++) {
			int k, s;
			cin >> k >> s;
			ans = max(ans, (d - k) / (double)s);
		}
		printf("Case #%d: %.12f\n", qq + 1, d / ans);
	}
}
