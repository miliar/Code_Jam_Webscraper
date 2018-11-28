#include<stdio.h>
FILE *in = fopen("C-large.in", "r");
FILE *out = fopen("output.txt", "w");
int main() {
	long long int n, i, t = 1;
	long long int s, e,x,y,x1,y1;
	fscanf(in,"%lld", &n);
	for (i = 1; i <= n; i++) {
		fscanf(in,"%lld %lld", &s, &e);
		x = 0; y = s; x1 = 0; y1 = 1;
		t = 1;
		while (t < e) {
			long long int x2=0, y2=0,x3=0,y3=0;
			if (x == 0) {
				if (y % 2 == 1) y2 = y / 2;
				else { x2 = (y / 2)-1; y2 = x2 + 1; }
				if (y % 2 == 0) { x3 = y1; y3 = y1; }
				else { y3 = y1*2; }
				x = x2; y = y2; x1 = x3; y1 = y3;
				e -= t; t = t << 1;
				continue;
			}
			if (x % 2 == 0) { x2 = x / 2-1; y2 = x2+1; }
			else { x2 = x / 2; y2 = x2 + 1; }
			if (x % 2 == 0) { x3 = x1; y3 = x1 + (y1 * 2); }
			else { x3 = (x1 * 2) + y1; y3 = y1; }
			x = x2; y = y2; x1 = x3; y1 = y3;
			e -= t; t=t << 1;
		}
		if (e <= y1)  t = y; else t = x;
		if (t % 2 == 0) fprintf(out,"Case #%lld: %lld %lld\n", i,t / 2, t / 2 - 1); else fprintf(out,"Case #%lld: %lld %lld\n", i,t / 2, t / 2);
	}
	return 0;
}