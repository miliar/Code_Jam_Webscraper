#include <stdio.h>
#include <string.h>
#include <assert.h>

#define BUFF_SIZE (2000)
void solve()
{
	char buff[BUFF_SIZE];
	int k;
	scanf("%s %d", buff, &k);
	int nFlips = 0;
	int total = strlen(buff);
	fprintf(stderr, "Total: %d k=%d\n", total, k);
	for (int i = 0; i < total; i++) {
		if ('+' == buff[i]) {
			continue;
		}
		if (buff[i] != '-') {
			fprintf(stderr, "Not -: %d %c\n", i, buff[i]);
		}
		assert('-' == buff[i]);
		if (i+k > total)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		++nFlips;
		for (int jk = 0; jk < k; jk++)
		{
			char before = buff[i+jk];
			assert ('-' == before || '+' == before);
			char after = '+' == before ? '-' : '+';
			buff[i+jk] = after;
		}
	}
	printf("%d\n", nFlips);
	return;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);
		solve();
	}
	return 0;
}
