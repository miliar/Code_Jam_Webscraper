#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

const int maxn = 1050;
int k;
char str[maxn];

void solve(int testcase) {
	scanf("%s%d", str, &k);
	int n = strlen(str);
	int cnt = 0;
	for (int i = 0; i + k <= n; i ++) {
		if (str[i] == '-') {
			cnt ++;
			for (int j = i; j < i + k; j ++) {
				if (str[j] == '-') str[j] = '+';
				else str[j] = '-';
			}
		}
	}
	for (int i = 0; i < n; i ++) {
		if (str[i] == '-') {
			cnt = -1;
		}
	}
	if (cnt == -1) printf("Case #%d: IMPOSSIBLE\n", testcase);
	else printf("Case #%d: %d\n", testcase, cnt);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++) {
		solve(i);
	}
	return 0;
}