#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <omp.h>
#include <algorithm>
using namespace std;
const int mn = 300, mt = 1441, INF = 0x3f3f3f3f;

struct activity {
	int st, ed;
	int id;
} a[mn];

bool cmp(activity a, activity b) {
	return a.st < b.st;
}

int f[mt][mt + 10][2][2];

int main() {
	int Tn;
	scanf("%d", &Tn);

	for (int Tc = 1; Tc <= Tn; ++Tc) {
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &a[i].st, &a[i].ed);
			a[i].id = 0;
		}
		for (int i = 0; i < m; ++i) {
			scanf("%d%d", &a[i + n].st, &a[i + n].ed);
			a[i + n].id = 1;
		}
		sort(a, a + n + m, cmp);

		memset(f, 0x3f, sizeof(f));

		for (int tmd = 0; tmd <= 1; ++tmd) {
			int p = 0;
			f[0][1][0][tmd] = (a[p].id == 1 || a[p].st > 0) ? tmd != 0 : INF;
			f[0][0][1][tmd] = (a[p].id == 0 || a[p].st > 0) ? tmd != 1 : INF;

//			f[0][1][1][0] = (a[p].id == 0 || a[p].st > 0) ? 1 : INF;
//			f[0][0][0][1] = (a[p].id == 1 || a[p].st > 0) ? 1 : INF;

			for (int i = 1; i < mt; ++i) {
				if (p < m + n && a[p].ed <= i) {
//				cout << "i = " << i << " p=" << p << endl;
					++p;
				}
				for (int j = 0; j <= i + 1; ++j) {
					for (int k = 0; k <= 1; ++k) {
						f[i][j][k][tmd] = INF;
						if (j == 0 && k == 0)
							continue;
//					if (i == 540 && j == 540 && k == 1) {
//						cout << (p >= m + n || a[p].st > i || a[p].id != k) << (p == 0 || a[p - 1].ed < i || a[p - 1].id != k) << endl;
//						cout << (p >= m + n || a[p].st > i || a[p].id != k) << (p == 0 || a[p - 1].ed < i || a[p - 1].id != 1 - k) << endl;
//					}
						if (p >= m + n || a[p].st > i || a[p].id != k)
							if (p == 0 || a[p - 1].ed < i || a[p - 1].id != k)
								f[i][j][k][tmd] = min(f[i - 1][j - (k == 0)][k][tmd],
										f[i][j][k][tmd]);
						if (p >= m + n || a[p].st > i || a[p].id != k)
							if (p == 0 || a[p - 1].ed < i
									|| a[p - 1].id != 1 - k)
								f[i][j][k][tmd] = min(
										f[i - 1][j - (k == 0)][1 - k][tmd] + 1,
										f[i][j][k][tmd]);
					}
				}
			}
		}

		int ans = min(min(f[1439][720][0][0], f[1439][720][1][1]), min(f[1439][720][0][1] + 1, f[1439][720][1][0] + 1));

//		while (1) {
//			int a, b, c;
//			cin >> a >> b >> c;
//			if (c >= 0)
//				cout << f[a][b][c] << endl;
//			else
//				break;
//		}
		printf("Case #%d: ", Tc);
		printf("%d\n", ans);
	}
	return 0;
}
