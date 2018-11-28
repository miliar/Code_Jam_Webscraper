#include <bits/stdc++.h>

#define maxn 100000008
#define pp push_back
#define pf push_front
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main(int argc, char *argv[])
{
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int d, n;
		scanf("%d %d", &d, &n);
		double ans = 0;
		for (int i = 0; i < n; ++i) {
			int k, s;
			scanf("%d %d", &k, &s);
			ans = max(double(d-k)/s, ans);
		}
		printf("Case #%d: %f\n", tt, d/ans);
	}
	return 0;
}
