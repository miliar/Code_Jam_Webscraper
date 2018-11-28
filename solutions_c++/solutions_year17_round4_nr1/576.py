#include <cstdio>
#include <algorithm>

using namespace std;

const int maxN = 110;

int f2[maxN], f3[maxN][maxN], f4[maxN][maxN][maxN];
int a[4];
double D, v, x;
int T;

void dof2(){
	memset(f2, 0, sizeof(f2));
	f2[0] = 0;
	for (int i=0;i<=100;++i) {
		f2[i + 2] = max(f2[i + 2], f2[i] + 1);
	}
}

void dof3() {
	memset(f3, 0, sizeof(f3));
	f3[0][0] = 0;
	for (int i=0;i<=100;++i)
		for (int j=0;j<=100;++j) {
			f3[i + 1][j + 1] = max(f3[i + 1][j + 1], f3[i][j] + 1);
			f3[i + 3][j] = max(f3[i + 3][j], f3[i][j] + 1);
			f3[i][j + 3] = max(f3[i][j + 3], f3[i][j] + 1);
		}
}

void dof4() {
	memset(f4, 0, sizeof(f4));
	f4[0][0][0] = 0;
	for (int i=0;i<=100;++i)
		for (int j=0;j<=100;++j)
			for (int k=0;k<=100;++k) {
				f4[i + 1][j][k + 1] = max(f4[i + 1][j][k + 1], f4[i][j][k] + 1);
				f4[i + 2][j + 1][k] = max(f4[i + 2][j + 1][k], f4[i][j][k] + 1);
				f4[i + 4][j][k] = max(f4[i + 4][j][k], f4[i][j][k] + 1);
				f4[i][j + 2][k] = max(f4[i][j + 2][k], f4[i][j][k] + 1);
				f4[i][j][k + 4] = max(f4[i][j][k + 4], f4[i][j][k] + 1);
			}
}

int main() {
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out","w",stdout);

	dof2();dof3();dof4();
	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii) {
		int N, P;
		printf("Case #%d: ", ii);
		scanf("%d %d", &N, &P);
		memset(a, 0, sizeof(a));
		for (int i=0;i<N;++i) {
			int x;
			scanf("%d", &x);
			a[x % P] ++;
		}
		int res = 0;
		if (P == 2) {
			for (int i = 0;i<=a[1];++i) {
				int _res = f2[i] + a[0];
				if (i < a[1]) ++_res;
				res = max(res, _res);
			}
		}
		if (P == 3) {
			for (int i = 0;i<=a[1];++i)
				for (int j=0;j<=a[2];++j) {
					int _res = f3[i][j] + a[0];
					if (i < a[1] || j < a[2]) ++_res;
					res = max(res, _res);
				}
		}
		if (P == 4) {
			for (int i = 0;i<=a[1];++i)
				for (int j=0;j<=a[2];++j)
					for (int k=0;k<=a[3];++k) {
						int _res = f4[i][j][k] + a[0];
						if (i < a[1] || j < a[2] || k < a[3]) ++_res;
						res = max(res, _res);
					}
		}

		printf("%d\n", res);
	}

	return 0;
}