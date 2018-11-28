#include <cstdio>
using namespace std;

int r, c;
char cake[50][50];

void fill_row(int fi) {
	int fj = 0;
	for (fj=0; fj<c; ++fj)
		if (cake[fi][fj] != '?') break;
	char sample = cake[fi][fj];
	for (int j=0; j<c; ++j) {
		if (cake[fi][j] != '?') sample = cake[fi][j];
		cake[fi][j] = sample;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		scanf("%d%d", &r, &c);
		for (int i=0; i<r; ++i)
			scanf("%s", cake[i]);

		int fi = 0;
		for (fi=0; fi<r; ++fi) {
			int fj = 0;
			for (fj=0; fj<c; ++fj)
				if (cake[fi][fj] != '?') break;
			if (fj < c) break;
		}
		fill_row(fi);
		for (int i=0; i<fi; ++i)
			for (int j=0; j<c; ++j)
				cake[i][j] = cake[fi][j];
		for (int i=fi+1; i<r; ++i) {
			int fj = 0;
			for (fj=0; fj<c; ++fj)
				if (cake[i][fj] != '?') break;
			if (fj >= c) {
				for (int j=0; j<c; ++j)
					cake[i][j] = cake[fi][j];
			} else {
				fi = i;
				fill_row(fi);
			}
		}
		printf("Case #%d: \n", TN);
		for (int i=0; i<r; ++i)
			puts(cake[i]);
	}
	return 0;
}
