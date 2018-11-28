#include <stdio.h>
#include <string.h>
#define MAX 1100

char c[MAX];
int n;
int k;

int main () {
  int teste;
  scanf ("%d", &teste);
  for (int t = 0; t < teste; t++) {
	scanf ("%s %d", &c, &k);
	n = strlen(c);
	int ret = 0;
	for (int i = 0; i <= n - k; i++) {
	  if (c[i] == '-') {
		ret++;
		for (int j = i; j < i + k; j++) {
		  if (c[j] == '-')
			c[j] = '+';
		  else
			c[j] = '-';
		}
	  }
	}
	printf ("Case #%d: ", t + 1);
	int flag = 0;
	for (int i = 0; i < n; i++)
	  if (c[i] == '-')
		flag = 1;
	if (flag)
	  printf ("IMPOSSIBLE\n");
	else
	  printf ("%d\n", ret);
  }
  return 0;
}
