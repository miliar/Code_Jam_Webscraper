#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char ch[1010];
int k;

void flip(int st) {
	for (int i = st; i < st + k; ++i) {
		if (ch[i] == '+') ch[i] = '-';
		else ch[i] = '+';
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int it = 1; it <= T; ++it) {
		scanf("%s%d", ch, &k);
		int n = strlen(ch), ans = 0;
		for (int i = 0; i <= n - k; ++i) {
			if (ch[i] == '-') {
				flip(i);
				ans ++;
			}
		}
		bool ok = true;
		for (int i = n - 1;i >= 0; --i)
			if (ch[i] == '-') ok = false;
		if (!ok) printf("Case #%d: IMPOSSIBLE\n", it);
		else printf("Case #%d: %d\n", it, ans);
	}
}
