#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;

int main() {
	int tt;
	double d, n, k, s, mx = -1.0;
	scanf("%d", &tt);
	for (int t = 0; t < tt; t++) {
		mx = -1.0;
		scanf("%lf %lf", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%lf %lf", &k, &s);
			mx = max(mx, (d-k)/s);
		}
		printf("Case #%d: %.9lf\n", t+1, d/mx);
	}	

	return 0;
}