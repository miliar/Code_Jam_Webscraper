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
char s[111];
int main() {
	//freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large-ans.out", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		scanf(" %s", s);
		int n = strlen(s);
		bool zero = 0;
		printf("Case #%d: ", ca++);
		rep(i, n - 1) {
			if (s[i] > s[i + 1]) {
				int x = i;
				while (x - 1 >= 0 && s[x - 1] == s[i]) --x;
				--s[x];
				for (int j = x + 1; j < n; ++j) s[j] = '9';
				break;
			}
		}
		rep(i, n) {
			if (s[i] != '0') {
				for (int j = i; j < n; ++j) putchar(s[j]);
				puts("");
				break;
			}
		}
	}
	return 0;
}

