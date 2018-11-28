#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char ch[20];

void fix(int k) {
	if (k == 0) return;
	if (ch[k] >= ch[k-1]) return;
	ch[k] = '9';
	ch[k-1] --;
	fix(k-1);
}

long long get() {
	long long ret = 0;
	for (int i = 0; i < strlen(ch); ++i)
		ret = ret * 10 + ch[i]-'0';
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int it = 1; it <= T; ++it) {
		scanf("%s", ch);
		int n = strlen(ch);
		for (int j = 1; j < n; ++j) {
			if (ch[j] >= ch[j-1]) continue;
			fix(j);
			for (int k = j + 1; k < n; ++k) ch[k] = '9';
			break;
		}
		long long ans1 = get();
		long long ans2 = 0ll;
		for (int i = 1; i < n; ++i)
			ans2 = ans2 * 10 + 9;
		long long ans = max(ans1, ans2);
		printf("Case #%d: %lld\n", it, ans);
	}

}
