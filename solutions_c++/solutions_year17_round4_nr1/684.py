#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
using namespace std;

int tn, N, P;
int a[101][101][101]; // 1, 2, 3

int main() {

	scanf("%d", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		memset(a, 0, sizeof(a));
		scanf("%d %d", &N, &P);
		int count_fullsize = 0;
		int icnt1 = 0, icnt2 = 0, icnt3 = 0;
		for(int i = 0; i < N;  i++) {
			int t = 0;
			scanf("%d", &t);
			switch (t % P) {
				case 0: count_fullsize ++; break;
				case 1: icnt1 ++; break;
				case 2: icnt2 ++; break;
				case 3: icnt3 ++; break;
			}
		}

		a[icnt1][icnt2][icnt3] = 0;
		for(int i = icnt1; i >= 0; i--)
			for(int j = icnt2; j >= 0; j--)
				for(int k = icnt3; k >= 0; k--) {
					int leftover = ((P-1)*(icnt1-i) + (P-2)*(icnt2-j) + (P-3)*(icnt3-k)) % P;
					int t = a[i][j][k] + (leftover == 0);
					// use modulo 1
					if (i > 0 && t > a[i-1][j][k]) a[i-1][j][k] = t;
					// use modulo 2
					//int t2 = (leftover == 2)? (t+1) : t;
					if (j > 0 && t > a[i][j-1][k]) a[i][j-1][k] = t;
					// use modulo 3
					//int t3 = (leftover == 3)? (t+1) : t;
					if (k > 0 && t > a[i][j][k-1]) a[i][j][k-1] = t;
				}

		printf("Case #%d: %d\n", ctn+1, a[0][0][0] + count_fullsize);

	}

	return 0;

}