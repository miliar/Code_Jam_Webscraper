#include <cstdio>
#include <cstring>
using namespace std;

int t, r, c;
char map[30][30];
bool chk[30];

int main(void) {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d:\n", iter);
		fscanf(fin, "%d%d", &r, &c);
		for (int i = 0; i < r; i++)
			fscanf(fin, "%s", map[i]);
		memset(chk, false, sizeof(chk));

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (map[i][j] == '?') continue;
				if (chk[map[i][j]-'A']) continue;

				chk[map[i][j]-'A'] = true;
				int rf, cf;
				for (rf = i; rf >= 1; rf--)
					if (map[rf - 1][j] != '?')
						break;
				for (cf = j; cf >= 1; cf--) {
					bool flag = true;
					for (int k = rf; flag && k <= i; k++)
						if (map[k][cf - 1] != '?')
							flag = false;
					if (!flag) 
						break;
				}
					
				int rt, ct;

				for (ct = j; ct < c - 1; ct++) {
					bool flag = true;
					for (int k = rf; flag && k <= i; k++)
						if (map[k][ct+1] != '?')
							flag = false;
					if (!flag)
						break;
				}

				for (rt = i; rt < r - 1; rt++) {
					bool flag = true;
					for (int k = cf; flag && k <= ct; k++)
						if (map[rt + 1][k] != '?')
							flag = false;
					if (!flag)
						break;
				}

				for (int ii = rf; ii <= rt; ii++)
					for (int jj = cf; jj <= ct; jj++)
						map[ii][jj] = map[i][j];
			}

		for (int i = 0; i < r; i++)
			fprintf(fout, "%s\n", map[i]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}