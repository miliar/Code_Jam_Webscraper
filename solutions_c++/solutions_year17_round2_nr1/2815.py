#include <cstdio>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#define gc getchar()

using namespace std;

int readInt() {
	int num = 0, ch;
	ch = gc;
	while (ch < '0' || ch > '9')
		ch = gc;
	while ('0' <= ch && ch <= '9') {
		num = (num << 3) + (num << 1) + ch - '0';
		ch = gc;
	}
	return num;
}

int main()
{
	int t = readInt();
	for (int j = 1; j <= t; j++) {
		int d, n;
		d = readInt();
		n = readInt();
		double ma = -1.0;
		for (int i = 0; i < n; i++) {
			int d1, s;
			d1 = readInt();
			s = readInt();
			double a = (d - d1)/(double)s;
			if (a > ma) {
				ma = a;
			}
		}
		printf("Case #%d: %0.6lf\n", j, d/ma);
	}
	return 0;
}

