#include<stdio.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int t;

int main() {
	fscanf(in,"%d", &t);
	for (int tc = 0; tc < t; tc++) {

		string str;
		int n, r, o, y, g, b, v;
		fscanf(in, "%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		if ((o != 0 && b <= o) || (r != 0 && r <= g) || (y != 0 && y <= v)) {
			fprintf(out, "Case #%d: IMPOSSIBLE\n", tc + 1);
			continue;
		}

		int aa = b - o - 1;
		int bb = r - g - 1;
		int cc = y - v - 1;
		b -= o + 1;
		r -= g + 1;
		y -= v + 1;
		if (o == 0) {
			b++;
			aa++;
		}
		if (g == 0) {
			r++;
			bb++;
		}
		if (v == 0) {
			y++;
			cc++;
		}
		if (aa + bb + cc - max(aa, max(bb, cc))<max(aa, max(bb, cc))) {
			fprintf(out, "Case #%d: IMPOSSIBLE\n", tc + 1);
			continue;

		}
		char last = 'Y';
		for (int i = 0; i < o; i++) {
			str+="BO";
		}

		if (o != 0) {
			str += "B";
			last = 'B';
		}
		for (int i = 0; i < g; i++) {

			str += "RG";
		}
		if (g != 0) {
			str += "R";
			last = 'R';
		}



		for (int i = 0; i < v; i++) {

			str += "YV";
		}

		if (v!= 0) {
			str += "Y";
			last = 'Y';
		}
		bool flag = 0;
		while (1) {
			if (b == 0 && r == 0 && y == 0)break;
			if (last == 'Y') {
				if (r > b) {
					last = 'R';
					r--;
				}			
				else{
					last = 'B';
					b--;
				}
			}
			else if (last == 'B') {
				if (y > r) {
					last = 'Y';
					y--;
				}
				else {
					last = 'R';
					r--;
				}
			}
			else  if (last == 'R') {
				if (y > b) {
					last = 'Y';
					y--;
				}
				else {
					last = 'B';
					b--;
				}
			}

			str += last;
		}
		fprintf(out,"Case #%d: %s\n", tc + 1, str.c_str());
	}
	return 0;
}