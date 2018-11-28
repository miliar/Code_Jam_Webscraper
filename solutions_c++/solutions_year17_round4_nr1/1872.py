#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 110

int n, p, a[MAXN];

int main () {
  int teste;
  scanf ("%d", &teste);
  for (int t = 0; t < teste; t++) {
	scanf ("%d %d", &n, &p);
	for (int i = 0; i < n; i++) {
	  scanf ("%d", &a[i]);
	}
	int ret = -1;
	if (p == 2) {
	  int impar = 0;
	  for (int i = 0; i < n; i++)
		if (a[i]%2)
		  impar++;
	  ret = n - (impar/2);
	}
	if (p == 3) {
	  int r0, r1, r2;
	  r0 = r1 = r2 = 0;
	  for (int i = 0; i < n; i++) {
		if (a[i]%3 == 0)
		  r0++;
		if (a[i]%3 == 1)
		  r1++;
		if (a[i]%3 == 2)
		  r2++;
	  }
	  int rm = min(r1, r2);
	  r1 -= rm;
	  r2 -= rm;
	  ret = r0 + rm + (r1/3) + (r1%3 != 0);
	  ret += (r2/3) + (r2%3 != 0);
	}
	if (p == 4) {
	  int r0, r1, r2, r3;
	  r0 = r1 = r2 = r3 = 0;
	  for (int i = 0; i < n; i++) {
		if (a[i]%4 == 0)
		  r0++;
		if (a[i]%4 == 1)
		  r1++;
		if (a[i]%4 == 2)
		  r2++;
		if (a[i]%4 == 3)
		  r3++;
	  }
	  int rm = min(r1, r3);
	  r1 -= rm;
	  r3 -= rm;
	  ret = r0 + rm + (r2/2) + (r1 + r3)/4;
	  r2 = r2%2;
	  r1 = (r1 + r3)%4;
	  if ((r2%2) && (r1%4 == 2)) {
		ret += (r2%2)*(r1%4 == 2);
		r2 = 0;
		r1 -= 2;
	  }
	  if (r2 > 0 || r1 > 0)
		ret++;
	}
	printf ("Case #%d: %d\n", t + 1, ret);
  }
  return 0;
}
