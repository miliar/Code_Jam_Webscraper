#include <cstdio>

using namespace std;

char firstId(char *crow, int len) {
	for (int i = 0; i < len; i++)
		if (crow[i] != '?')
			return crow[i];
	return '?';
}

void copy(char cake[43][43], int len, int from, int to) {
	for (int i = 0; i < len; i++)
		cake[to][i] = cake[from][i];
}


void proc(int cn) {
	int row, col;
	char cake[43][43];

	scanf("%d %d", &row, &col);
	for (int i = 0; i < row; i++)
		scanf("%s", cake[i]);

	int firstRow;
	for (firstRow = 0; firstRow < row && firstId(cake[firstRow], col) == '?'; firstRow++);

	for (int i = firstRow; i < row; i++) {
		char lastId = firstId(cake[i], col);
		if (lastId != '?') {
		for (int j = 0; j < col; j++) {
			if (cake[i][j] == '?')
				cake[i][j] = lastId;
			else
				lastId = cake[i][j];
		}
		} else
			copy(cake, col, i - 1, i);
	}

	for (int i = firstRow - 1; i >= 0; i--)
		copy(cake, col, firstRow, i);


	printf("Case #%d:\n", cn);
	for (int i = 0; i < row; i++)
		printf("%s\n", cake[i]);
}

int main() {
	int nc;
	scanf("%d", &nc);
	for (int i = 0; i < nc; i++)
		proc(i + 1);
	return 0;

}
