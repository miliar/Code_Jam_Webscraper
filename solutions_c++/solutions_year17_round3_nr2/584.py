#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
	int act[1450];
	int dy[3][3][1450];

	int i, j, k;

	int T;
	char buf[512];

	fgets(buf, 512, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		memset(act, 0x00, sizeof(act));
		memset(dy, 1, sizeof(dy));

		int AC, AJ;

		fgets(buf, 512, stdin);
		sscanf(buf, "%d %d", &AC, &AJ);

		for (j = 0; j < AC; ++j) {
			int st, en;
			fgets(buf, 512, stdin);
			sscanf(buf, "%d %d", &st, &en);

			for (k = st; k < en; ++k) {
				act[k] = 1;
			}
		}

		for (j = 0; j < AJ; ++j) {
			int st, en;
			fgets(buf, 512, stdin);
			sscanf(buf, "%d %d", &st, &en);

			for (k = st; k < en; ++k) {
				act[k] = 2;
			}
		}

		int MAXV = 5000;

		dy[1][1][0] = 0;
		dy[1][2][0] = MAXV;
		dy[2][1][0] = MAXV;
		dy[2][2][0] = 0;

		for (j = 0; j < 1440; ++j) {
			if (act[j] == 0) {
				for (k = min(j, 722); k >= 0; --k) {
					dy[1][1][k+1] = min(dy[1][1][k], dy[1][1][k+1]);
					dy[1][1][k+1] = min(dy[1][2][k] + 1, dy[1][1][k+1]);

					dy[1][2][k] = min(dy[1][1][k] + 1, dy[1][2][k]);
					dy[1][2][k] = min(dy[1][2][k], dy[1][2][k]);

					dy[2][1][k+1] = min(dy[2][1][k], dy[2][1][k+1]);
					dy[2][1][k+1] = min(dy[2][2][k] + 1, dy[2][1][k+1]);

					dy[2][2][k] = min(dy[2][1][k] + 1, dy[2][2][k]);
					dy[2][2][k] = min(dy[2][2][k], dy[2][2][k]);

					//cout << j << " " << j + 1 << " ==> " << "a1 works " << k + 1 << " " << dy[1][1][k+1] << " and " << dy[2][1][k+1] << endl;
					//cout << j << " " << j + 1 << " ==> " << "c1 works " << k << " " << dy[1][2][k] << " and " << dy[2][2][k] << endl;

					dy[1][1][k] = MAXV;
					dy[2][1][k] = MAXV;
				}
			} else if (act[j] == 2) {
				for (k = min(j, 722); k >= 0; --k) {
					dy[1][1][k+1] = min(dy[1][1][k], dy[1][1][k+1]);
					dy[1][1][k+1] = min(dy[1][2][k] + 1, dy[1][1][k+1]);

					dy[1][2][k] = MAXV;

					dy[2][1][k+1] = min(dy[2][1][k], dy[2][1][k+1]);
					dy[2][1][k+1] = min(dy[2][2][k] + 1, dy[2][1][k+1]);

					dy[2][2][k] = MAXV;

					//cout << j << " " << j + 1 << " ==> " << "a2 works " << k + 1 << " " << dy[1][1][k+1] << " and " << dy[2][1][k+1] << endl;
					//cout << j << " " << j + 1 << " ==> " << "c2 works " << k << " " << dy[1][2][k] << " and " << dy[2][2][k] << endl;

					dy[1][1][k] = MAXV;
					dy[2][1][k] = MAXV;
				}
			} else if (act[j] == 1) {
				for (k = min(j, 722); k >= 0; --k) {
					dy[1][1][k+1] = MAXV;

					dy[1][2][k] = min(dy[1][1][k] + 1, dy[1][2][k]);
					dy[1][2][k] = min(dy[1][2][k], dy[1][2][k]);

					dy[2][1][k+1] = MAXV;

					dy[2][2][k] = min(dy[2][1][k] + 1, dy[2][2][k]);
					dy[2][2][k] = min(dy[2][2][k], dy[2][2][k]);

					//cout << j << " " << j + 1 << " ==> " << "a3 works " << k + 1 << " " << dy[1][1][k+1] << " and " << dy[2][1][k+1] << endl;
					//cout << j << " " << j + 1 << " ==> " << "c3 works " << k << " " << dy[1][2][k] << " and " << dy[2][2][k] << endl;

					dy[1][1][k] = MAXV;
					dy[2][1][k] = MAXV;
				}
			}
		}

		printf("Case #%d: %d\n", i + 1, min(dy[1][1][720], dy[2][2][720]));
	}
}