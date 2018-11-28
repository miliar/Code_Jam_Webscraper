#include <cstdio>
using namespace std;
typedef long long ll;

const int MAX_S = 1000;

int solve() {
	bool s[MAX_S];
	bool flipped[MAX_S] = {};
	int k;

	int len = 0;
	for (int c=getchar(); c!=' '; c=getchar()) {
		s[len++] = c=='-';
	}
	scanf("%d\n", &k);

	bool acc = false;
	int ans = 0;
	for (int i=0; i<len-k+1; i++) {
		if (s[i] ^ acc) {
			flipped[i] = true;
			ans++;
			acc = !acc;
		}
		if (i>=k-1 && flipped[i-k+1]) {
			acc = !acc;
		}
	}
	for (int i=len-k+1; i<len; i++) {
		if (s[i] ^ acc) {
			return -1;
		}
		if (i>=k-1 && flipped[i-k+1]) {
			acc = !acc;
		}
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	getchar();
	for (int i=1; i<=t; i++) {
		int ans = solve();
		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		} else {
			printf("Case #%d: %d\n", i, ans);
		}
	}
}
