#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long LL;

LL n;

void solve(int tim) {
	printf("Case #%d: ", tim);
	scanf("%lld", &n);
	for (LL i = n; i; i --) {
		LL lst = 10;
		bool ok = 1;
		for (LL x = i; x; x /= 10) {
			if (x % 10 > lst) {
				ok = 0;
				break;
			}
			lst = x % 10;			
		}
		if (ok) {
			printf("%lld\n", i);
			return;
		}
	}
}

int main() {
	//freopen("B.in", "r", stdin), freopen("B.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}