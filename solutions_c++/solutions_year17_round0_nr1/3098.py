#include <cstdio>
#include <cstring>

#define MAXN (1 << 10)

int testCount;
int n, k;
char s[MAXN];

int main() {
	scanf("%d", &testCount);
	for (int test = 1; test <= testCount; ++test) {
		scanf("%s %d", s, &k);
		n = strlen(s);		
		int flips = 0;
		for (int i = 0; i < n && (i + k - 1) < n; ++i)
			if (s[i] == '-') {
				flips++;
				for (int j = 0; j < k; ++j)
					s[i+j] = (s[i+j] == '+') ? '-' : '+';
			}			
		for (int i = 0; i < n; ++i) if (s[i] == '-') flips = -1;		
		printf("Case #%d: ", test);
		if (flips < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", flips);
		
	}
	return 0;
}
