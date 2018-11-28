#include <cstdio>
#include <cstring>

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

char s[100];

int main() {
	int tcs;
	scanf("%d", &tcs);
	FOR(tc, 1, tcs) {
		scanf("%s", s);
		int len = strlen(s), start = -1;
		REP(i, len-1) {
			if (i == 0 || s[i] != s[i-1]) {
				start = i;
			}
			if (s[i] > s[i+1]) {
				s[start]--;
				FOR(j, start+1, len-1) {
					s[j] = '9';
				}
				break;
			}
		}
		printf("Case #%d: %s\n", tc, s + (s[0] == '0' ? 1 : 0));
	}
	return 0;
}
