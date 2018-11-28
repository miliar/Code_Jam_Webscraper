#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 11111;
char s[N];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large-ans.out", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		int k;
		scanf(" %s %d", s, &k);
		int n = strlen(s);
		int cnt = 0;
		rep(i, n - k + 1) {
			if (s[i] == '-') {
				++cnt;
				rep(j, k) {
					s[i + j] = (s[i + j] == '+' ? '-' : '+');
				}
			}
		}
		bool ok = 1;
		rep(i, n) if (s[i] != '+') ok = 0;
		printf("Case #%d: ", ca++);
		if (ok) {
			printf("%d\n", cnt);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}

