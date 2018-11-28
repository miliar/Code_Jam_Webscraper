#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

int solve(int p, int r1, int r2, int *q1, int *q2, vector <bool> q1_, vector <bool> q2_, int ii) {

	int max = 0;

	for ( int i = ii; i < p; ++i ) {
		if ( q1_[i] ) continue;
		for ( int j = 0; j < p; ++j ) {
			if ( q2_[j] ) continue;
			int maxc1 = (100*q1[i]) / (90*r1);
			int maxc2 = (100*q2[j]) / (90*r2);
			int minc1 = (100*q1[i]) / (110*r1) + ((100*q1[i]) % (110*r1) ? 1 : 0);
			int minc2 = (100*q2[j]) / (110*r2) + ((100*q2[j]) % (110*r2) ? 1 : 0);
			if ( maxc1 < minc1 || maxc2 < minc2 ) continue;
			if ( ( minc1 <= maxc2 && maxc1 >= minc2 ) || ( minc2 <= maxc1 && maxc2 >= minc1 ) ) {
				vector <bool> q1__ = q1_;
				vector <bool> q2__ = q2_;
				q1__[i] = true;
				q2__[j] = true;
				int nmax = 1+solve(p, r1, r2, q1, q2, q1__, q2__, i+1);
				if (nmax > max) max = nmax;
			}
		}
	}

	return max;

}

int solve1(int p, int r, int *q) {

	int c = 0;

	for ( int i = 0; i < p; ++i ) {

		int max = (100*q[i]) / (90*r);
		int min = (100*q[i]) / (110*r) + ((100*q[i]) % (110*r) ? 1 : 0);

		if ( max < min ) continue;
		++c;
	}

	return c;

}

int main() {

	int _t;
	scanf("%d", &_t);

	for ( int t = 0; t < _t; ++t ) {

		int n, p;
		scanf("%d %d", &n, &p);

		if (n > 2) abort();

		int r1;
		int r2;
		if (n == 2)
		scanf("%d %d", &r1, &r2);
		else
		scanf("%d", &r1);

		int q1[8];
		int q2[8];

		for ( int i = 0; i < p; ++i )
			scanf("%d", &q1[i]);
		if ( n == 2 )
		for ( int i = 0; i < p; ++i )
			scanf("%d", &q2[i]);

		if ( n == 2 )
		printf("Case #%d: %d\n", t+1, solve(p, r1, r2, q1, q2, vector <bool>(p, false), vector <bool>(p, false), 0));
		else
		printf("Case #%d: %d\n", t+1, solve1(p, r1, q1));

	}

}
