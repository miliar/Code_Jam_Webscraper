#include <stdio.h>
#include <string.h>
#define MAX 110

char c[MAX];
int d[MAX], n;

int main () {
  int test;
  scanf ("%d", &test);
  for (int t = 0; t < test; t++) {
	printf ("Case #%d: ", t + 1);
	scanf ("%s", &c);
	n = strlen(c);
	for (int i = 0; i < n; i++)
	  d[i] = c[i] - '0';
	int dec = -1;
	for (int i = 0; i < n - 1; i++) {
	  if (d[i] > d[i + 1]) {
		dec = i;
		break;
	  }
	}
	if (dec == -1) {
	  printf ("%s\n", c);
	  continue;
	}
	while (dec > 0 && d[dec - 1] == d[dec])
	  dec--;
	if (dec == 0 && d[dec] == 1) {
	  for (int i = 0; i < n - 1; i++) {
		printf ("9");
	  }
	  printf ("\n");
	} else {
	  d[dec]--;
	  for (int i = dec + 1; i < n; i++)
		d[i] = 9;
	  for (int i = 0; i < n; i++)
		printf ("%d", d[i]);
	  printf ("\n");
	}
  }
  return 0;
}
