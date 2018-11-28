#include <bits/stdc++.h>
using namespace std;
#define ll long long
int T, n, m;
pair<int, int>a[10];
void solve(int test) {
	scanf("%d %d", &n, &m);
	for (int i=0; i<n+m; i++) scanf("%d %d", &a[i].first, &a[i].second);
	sort(a, a+n+m);
	printf("Case #%d: ", test);
	if (n+m==1) {
		printf("2\n");
	} else if (n==0||m==0) {
		if (a[1].second-a[0].first<=720) printf("2\n");
		else if (a[0].second+1440-a[1].first<=720)printf("2\n");
		else printf("4\n");
	} else {
		printf("2\n");
	}
}
int main () {
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
