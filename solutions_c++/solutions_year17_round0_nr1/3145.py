#include <cstdio>
using namespace std;

char buf[10001];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		int k;
		scanf("%s %d ", buf, &k);
		int ans = 0;
		for (int i=0; buf[i+k-1]; ++i) {
			if (buf[i] == '+') continue;
			for (int j=0; j<k; ++j)
				buf[i+j] = (buf[i+j] == '+') ? '-' : '+';
			++ans;
		}
		bool success = true;
		for (int i=0; buf[i]; ++i) {
			if (buf[i] == '-') {
				success = false;
				break;
			}
		}
		printf("Case #%d: ", TN);
		if (success) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}