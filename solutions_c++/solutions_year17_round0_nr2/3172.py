#include <stdio.h>
#include <string.h>
#include <assert.h>

#define DE(format, ...) fprintf(stderr,format, ##__VA_ARGS__)

#define BUFF_SIZE (100)

void tidy(char *buff);

void solve()
{
	char buff[BUFF_SIZE];
	scanf("%s", buff);
	DE("buff = %s\n", buff);
	tidy(buff);
}

void tidy(char *buff)
{
	for(int i = 0; i < strlen(buff) - 1; i++) {
		if (buff[i] <= buff[i+1]) {
			continue;
		}
		DE("Decreasing at i=%d, %c>%c\n", i, buff[i], buff[i+1]);
		--buff[i]; // Need recheck for buff[i-1]
		for (int k = i+1; k < strlen(buff); k++) {
			buff[k] = '9';
		}
		tidy(buff);
		return;
	}

	// all in order
	char *buff_print = buff;
	while ('0' == buff_print[0]) {
		++buff_print;
	}
	
	DE("result=%s\n", buff_print);
	printf("%s\n", buff_print);
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
