#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int t, n, p;
int rem[5];
int ans;

int main(void) {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		ans = 0;

		fscanf(fin, "%d%d", &n, &p);
		memset(rem, 0, sizeof(rem));

		for (int i = 0; i < n; i++) {
			int tmp; fscanf(fin, "%d", &tmp);
			rem[tmp%p]++;
		}

		ans = rem[0];
		if (p == 2)
			ans += (rem[1] + 1) / 2;
		else if (p == 3) {
			if (rem[1] >= rem[2]) {
				ans += rem[2];
				ans += (rem[1] - rem[2] + 2) / 3;
			}
			else {
				ans += rem[1];
				ans += (rem[2] - rem[1] + 2) / 3;
			}
		}
		else {
			ans += rem[2] / 2;
			rem[2] = rem[2] % 2;

			if (rem[1] >= rem[3]) {
				ans += rem[3];
				rem[1] -= rem[3];
				if (rem[2])
					ans += (rem[1] + 5) / 4;
				else
					ans += (rem[1] + 3) / 4;
			}
			else {
				ans += rem[1];
				rem[3] -= rem[1];
				if (rem[2])
					ans += (rem[3] + 5) / 4;
				else
					ans += (rem[3] + 3) / 4;
			}
		}
		fprintf(fout, "%d\n", ans);
	}
	return 0;
}