#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;

template<class T> inline
void read(T& x) {
	int f = 1; x = 0;
	char ch = getchar();
	while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
	while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
	x *= f;
}

/*============ Header Template ============*/

const int N = 1000 + 5;

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		char s[20];
		scanf("%s", s);
		int n = strlen(s);
		int begin = 0;
		for (int j = 1; j < n; ++j) {
			if (s[j] > s[j - 1]) {
				begin = j;
			} else if (s[j] < s[j - 1]) {
				--s[begin];
				for (int k = begin + 1; k < n; ++k) {
					s[k] = '9';
				}
			}
		}
		long long ans = 0;
		for (int j = 0; j < n; ++j) {
			ans = ans * 10 + s[j] - '0';
		}
		printf("Case #%d: %lld\n", i, ans);
	}
	return 0;
}