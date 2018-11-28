#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

void solve_large(long long n, long long k) {
	if (k <= 1) {
		long long le = (n - 1) / 2;
		long long ri = (n - 1) - (n - 1) / 2;
		printf("%lld %lld\n", max(le, ri), min(le, ri));
	}
	else {
		if (n & 1) {
			if ((k - 1) & 1)
				solve_large(n / 2, (k - 1) / 2 + 1);
			else
				solve_large(n / 2, (k - 1) / 2);
		}
		else {
			if ((k-1) & 1)
				solve_large(n / 2, (k - 1) / 2 + 1);
			else
				solve_large(n / 2 - 1 , (k - 1) / 2);
		}
	}
	
	
}

void solve() {
	long long n, k;
	scanf("%lld %lld", &n, &k);
	solve_large(n, k);
}

int main() {
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		printf("Case #%d: ", R);
		solve();
	}

}