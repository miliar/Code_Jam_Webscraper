// Problem A. Alphabet Cake
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

char a[32][32];

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int r, c;
		scanf("%d %d", &r, &c);
		for (int i = 0; i < r; i++) scanf("%s", a[i]);

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if (a[i][j] != '?') a[i][j] = a[i][j] - 'A' + 'a';

		for ( ; ; ) {
			int max_c = 0, max_a = 0, max_x, max_xx, max_y, max_yy;
			for (int x = 0; x < r; x++)
				for (int y = 0; y < c; y++)
					for (int xx = x; xx < r; xx++)
						for (int yy = y; yy < c; yy++) {
							int t = 0;
							bool ok = true;
							for (int i = x; i <= xx && ok; i++)
								for (int j = y; j <= yy && ok; j++) {
									if (a[i][j] == '?') continue;
									if (a[i][j] >= 'A' && a[i][j] <= 'Z') {
										ok = false;
										break;
									}
									if (t > 0 && a[i][j] != t) {
										ok = false;
										break;
									}
									t = a[i][j];
								}
							if (ok && t > 0) {
								int v = (xx - x + 1) * (yy - y + 1);
								if (v > max_a) {
									max_a = v;
									max_c = t - 'a' + 'A';
									max_x = x;
									max_xx = xx;
									max_y = y;
									max_yy = yy;
								}
							}
						}
			if (max_a <= 1) break;
			for (int i = max_x; i <= max_xx; i++)
				for (int j = max_y; j <= max_yy; j++)
					a[i][j] = max_c;

		}

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				if (a[i][j] >= 'a' && a[i][j] <= 'z')
					a[i][j] = a[i][j] - 'a' + 'A';

		printf("Case #%d:\n", ti);

		for (int i = 0; i < r; i++) printf("%s\n", a[i]);
	}

	return 0;
}
