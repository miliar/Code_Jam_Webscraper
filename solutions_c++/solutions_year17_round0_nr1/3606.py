#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

#define MAXN 1005

using namespace std;

int tt;
char s[MAXN];

int main() {
	FILE *fout, *fin;
	fout = fopen("aout.txt", "wb");
	fin = fopen("ain.txt", "r");
	fscanf(fin, "%d", &tt);
	for (int t = 1 ; t <= tt ; t ++) {
		int ans = 0, k;
		fscanf(fin, "%s %d", s, &k);
		int n = strlen(s);
		for (int i = 0 ; i < n ; i ++) {
			if (s[i] == '-') {
				if (i + k <= n) {
					ans ++;
					for (int j = i ; j < i + k ; j ++) {
						if (s[j] == '-') s[j] = '+';
						else s[j] = '-';
					}
				} else ans = -MAXN;
			}
		}
		if (ans >= 0) fprintf(fout, "Case #%d: %lld\n", t, ans);
		else fprintf(fout, "Case #%d: IMPOSSIBLE\n", t, ans);
	}
	fclose(fout);
	return 0;
}