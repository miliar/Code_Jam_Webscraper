#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

char s[1010];

int main() {
	int tcs;
	scanf("%d", &tcs);
	FOR(tc, 1, tcs) {
		int k;
		scanf("%s%d", s, &k);
		int len = strlen(s);
		int ans = 0;
		queue<int> ends;
		REP(i, len) {
			bool neg = ends.size() % 2 == 1;
			if (s[i] == (neg ? '+' : '-')) {
				ans++;
				ends.push(i + k - 1);
			}
			if (!ends.empty() && ends.front() == i) {
				ends.pop();
			}
		}
		printf("Case #%d: ", tc);
		if (!ends.empty()) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
