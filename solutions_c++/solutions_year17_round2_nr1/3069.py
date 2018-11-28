#include <cstdio>  
#include <algorithm>  
#include <cstring>  
using namespace std;
typedef long long ll;  
typedef pair<ll, ll> p;
p a[10002];
int d, n;
bool gao(double x) {
	for (int i = 0; i < n; i++) {
		double sec = d / x;
		if ((a[i].first + sec * a[i].second) < d) {
			return false;
		}
	}
	return true;
}
int main() {
	int t;
	freopen("A-large.in", "r", stdin);
 	freopen("outputA.out", "w", stdout);  
	scanf("%d", &t);
	for (int j = 1; j <=t; j++) {

		scanf("%d %ld", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%ld %ld", &(a[i].first), &(a[i].second));	
		}
		sort(a, a + n);
		double temp = (double)(d - a[0].first) / a[0].second;
		double lo = 0;
		double hi = d / temp;
		double mid;
		double ans = -1;
		if (n == 1) {
			printf("Case #%d: %lf\n", j, hi);
			continue;
		}
		while (lo < hi - 0.000001) {
			mid = (lo + hi) / 2;
			if (gao(mid)) {
				lo = mid;
				ans = mid;
			} else {
				hi = mid;
			}
		}
		printf("Case #%d: %lf\n", j, mid);
	}
    return 0;     
}   