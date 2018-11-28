#include <cstdio>
#include <cstring>

char N[20];

void solve() {
    int i, j, k, len;
    char N[20];
    scanf("%s", N);
    len = strlen(N);
    for (i = 0, j = -1; i + 1 < len && N[i] <= N[i + 1]; i++)
	if (N[i] < N[i + 1])
	    j = i;
    if (i == len - 1) {
	puts(N);
	return;
    }
    if (j == -1) {
	if (N[0] != '1')
	    putchar(N[0] - 1);
	for (k = 1; k < len; k++)
	    putchar('9');
	putchar('\n');
	return;
    }
    for (k = 0; k <= j; k++)
	putchar(N[k]);
    putchar(N[k] - 1);
    for (k = j + 2; k < len; k++)
	putchar('9');
    putchar('\n');
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
	printf("Case #%d: ", i);
	solve();
    }
}
