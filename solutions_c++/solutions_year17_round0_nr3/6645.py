#include<stdio.h>
FILE *in = fopen("C-small-1-attempt0.in", "r");
FILE *out = fopen("output.txt", "w");
void main() {
	int nii, i, t = 1;
	int s, eioi, x, y, x1, y1;
	fscanf(in, "%d", &nii);
	for (i = 1; i <= nii; i++) {
		fscanf(in, "%d %d", &s, &eioi);
		x = 0; y = s; x1 = 0; y1 = 1;
		t = 1;
		while (t < eioi)
		{
			int x2 = 0, y2 = 0, x3 = 0, y3 = 0;
			if (x == 0) 
			{
				if (y % 2 == 1) y2 = y / 2;
				if (y % 2 == 0) { x2 = (y / 2) - 1; y2 = x2 + 1; }
				if (y % 2 == 0) { x3 = y1; y3 = y1; }
				if (y % 2 == 1) { y3 = y1 * 2; }
				x = x2; y = y2; x1 = x3; y1 = y3;
				eioi -= t; t = t << 1;
				continue;
			}
			if (x % 2 == 1) { x2 = x / 2; y2 = x2 + 1; } 
			else { x2 = x / 2 - 1; y2 = x2 + 1; }
			if (x % 2 == 0) { x3 = x1; y3 = x1 + (y1 * 2); }
			else { x3 = (x1 * 2) + y1; y3 = y1; }
			x = x2; y = y2; x1 = x3; y1 = y3;
			eioi -= t; t = t << 1;
		}
		if (eioi <= y1)  t = y; else t = x;
		if (t % 2 == 0) fprintf(out, "Case #%d: %d %d\n", i, t / 2, t / 2 - 1); else fprintf(out, "Case #%d: %d %d\n", i, t / 2, t / 2);
	}
}