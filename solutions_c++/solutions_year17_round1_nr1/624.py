#include <stdio.h>
#define MAX 30

int r, c;
char a[MAX][MAX];

int main () {
  int test;
  scanf ("%d", &test);
  for (int t = 0; t < test; t++) {
	scanf ("%d %d", &r, &c);
	for (int i = 0; i < r; i++) {
	  scanf ("%s", &a[i]);
	}
	for (int i = 0; i < r; i++) {
	  char first = -1;
	  for (int j = 0; j < c; j++)
		if (a[i][j] != '?') {
		  first = a[i][j];
		  break;
		}
	  if (first == -1)
		continue;
	  char curr = first;
	  for (int j = 0; j < c; j++) {
		if (a[i][j] == '?') {
		  a[i][j] = curr;
		} else {
		  curr = a[i][j];
		}
	  }
	}
	int first = -1;
	for (int i = 0; i < r; i++) 
	  if (a[i][0] != '?') {
		first = i;
		break;
	  }
	int curr = first;	
	for (int i = 0; i < r; i++) {
	  if (a[i][0] == '?') {
		for (int j = 0; j < c; j++)
		  a[i][j] = a[curr][j];
	  } else {
		curr = i;
	  }
	}
	printf ("Case #%d:\n", t + 1);
	for (int i = 0; i < r; i++)
	  printf ("%s\n", a[i]);
  }
  return 0;
}
