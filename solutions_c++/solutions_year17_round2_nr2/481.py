#include<stdio.h>
#include<memory.h>
FILE *fo, *fp;
char l[1010];
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	for (t = 1; t <= T; t++) {
		int N, R, O, Y, G, B, V;
		fscanf_s(fo,"%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		fprintf_s(fp, "Case #%d: ", t);

		int r, y, b, max;
		bool check = true;
		memset(l, 0, sizeof(l));

		if (O * 2 > B || G * 2 > R || V * 2 > Y) {
			check = false;
		}
		else {
			r = R - G;
			b = B - O;
			y = Y - V;
			max = (r < b) ? b : r;
			if (max < y) max = y;

			if (max > r + b + y - max) {
				check = false;
			}
		}
		if (check) {
			// find	
			int i, tot = r + y + b;
			if (r >= y && r >= b) {
				l[0] = 'r';
				r--;
			}
			else if (y >= r && y >= b) {
				l[0] = 'y';
				y--;
			}
			else if (b >= r && b >= y) {
				l[0] = 'b';
				b--;
			}

			for (i = 1; i < tot; i++) {
				if (l[i - 1] == 'r') {
					if (y < b) {
						l[i] = 'b';
						b--;
					}
					else {
						l[i] = 'y';
						y--;
					}
				}
				else if (l[i - 1] == 'y') {
					if (r < b) {
						l[i] = 'b';
						b--;
					}
					else {
						l[i] = 'r';
						r--;
					}
				}
				else {
					if (y < r) {
						l[i] = 'r';
						r--;
					}
					else {
						l[i] = 'y';
						y--;
					}
				}
			}
			if (l[0] == l[tot - 1]) {
				int now = tot - 1 , tmp;
				while (now - 2 >= 0) {
					tmp = l[now];
					l[now] = l[now - 1];
					l[now - 1] = tmp;
					if (l[now - 2] != l[now - 1]) {
						break;
					}
					now--;
				}
			}
			for (i = 0; i < tot; i++) {
				if (l[i] == 'r') {
					if (G != 0) {
						G--;
						fprintf_s(fp,"RGR");
					}
					else {
						fprintf_s(fp, "R");
					}
				}
				else if (l[i] == 'b') {
					if (O != 0) {
						O--;
						fprintf_s(fp, "BOB");
					}
					else {
						fprintf_s(fp, "B");
					}
				}
				else if (l[i] == 'y') {
					if (V != 0) {
						V--;
						fprintf_s(fp, "VYV");
					}
					else {
						fprintf_s(fp, "Y");
					}
				}
			}
		}
		else {
			fprintf_s(fp, "IMPOSSIBLE");
		}
		fprintf_s(fp, "\n");
	}
	return 0;
}