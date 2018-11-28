#include <stdio.h>

int main() {
	int T, K, n[1010], i, j, c, w, t = 1; char s[1010];
	for (scanf("%d", &T); T--; printf(w ? "Case #%d: IMPOSSIBLE\n" : "Case #%d: %d\n", t++, c)) {
		for (scanf("%s%d", s, &K), i = 0; s[i]; i++)
			n[i] = (s[i] == '-' ? 1 : 0);
		for (c = i = 0; s[i+K-1]; i++)
			if (n[i]%2)
				for (c++, j = i; j < i+K; j++)
					n[j]++;
		for (w = 0; s[i]; i++)
			w += (n[i]%2);
	}
}
