#include <cstdio>
#include <cstdlib>
#include <cstring>

int r, c;

char mat[100][100];

void read() {
	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; i++) {
		scanf("%s", mat[i]);
	}
}

void process() {
	int lastRow = -1;
	for (int i = 0; i < r; i++) {
		int first = 0;
		while (first < c && mat[i][first] == '?') {
			first++;
		}
		if (first != c) {
			char last = mat[i][first];
			for (int j = 0; j < c; j++) {
				if (mat[i][j] != '?') {
					last = mat[i][j];
				}
				mat[i][j] = last;
			}
			if (lastRow == -1) {
				for (int k = 0; k < i; k++) {
					for (int j = 0; j < c; j++) {
						mat[k][j] = mat[i][j];
					}
				}
			}
			lastRow = i;
		} else if (lastRow != -1) {
			for (int j = 0; j < c; j++) {
				mat[i][j] = mat[lastRow][j];
			}
		}
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			printf("%c", mat[i][j]);
		}
		printf("\n");
	}
}

int main() {

	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d:\n", i);
		read();
		process();
	}
	
	return 0;
}