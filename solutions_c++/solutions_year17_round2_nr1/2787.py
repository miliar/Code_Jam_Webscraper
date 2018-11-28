#include<stdio.h>
#include<algorithm>
using namespace std;
FILE *in=fopen("A-large.in","r");
FILE *out = fopen("output.txt", "w");
struct data {
	inline bool operator <(const data &temp)const {
		return x<temp.x || (x == temp.x && y<temp.y);
	}
	int x, y;
}b[2000];
int main() {
	int t, i, x, n, k, j;
	double m;
	fscanf(in,"%d", &t);
	for (i = 1; i <= t; i++) {
		fscanf(in,"%d %d", &k, &n);
		for (j = 1; j <= n; j++) {
			fscanf(in,"%d %d", &b[j].x, &b[j].y);
		}
		sort(b + 1, b + n + 1);
		m = 0.0;
		for (j = n; j >= 1; j--) {
			if (m<(double)(k - b[j].x) / (double)(b[j].y)) m = (double)(k - b[j].x) / (double)(b[j].y);
		}
		fprintf(out,"Case #%d: %lf\n", i, (double)((double)(k) / m));
	}
	return 0;
}