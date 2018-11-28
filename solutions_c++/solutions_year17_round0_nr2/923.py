#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(void) {
	int t;
	scanf("%d", &t);
	for (int id = 1; id <= t; ++id) {
		char s[20];
		scanf("%s", s);
		int n = strlen(s);
		int begin = 0;
		for (int i = 1; i < n; ++i) {
			if (s[i] > s[i - 1]) begin = i;
			else if (s[i] < s[i - 1]) {
				--s[begin];
				while (++begin < n) {
					s[begin] = '9';
				}
			}
		}
		long long ans = 0;
		for (int i = 0; i < n; ++i) {
			ans = 10 * ans + s[i] - '0';
		}
		printf("Case #%d: %I64d\n", id, ans);
	}
	return 0;
}