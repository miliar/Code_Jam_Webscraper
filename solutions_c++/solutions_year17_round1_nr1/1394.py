#include <cstdio>

#define MAX 30

int main () {
	int t, r, c;
	char grid[MAX][MAX];
	scanf ("%d", &t);

	for (int k = 1; k <= t; k++) {
		scanf ("%d%d", &r, &c);
		for (int i = 0; i < r; i++)
			scanf ("%s", grid[i]);

		//left->right
		for (int i = 0; i < r; i++)
			for (int j = 1; j < c; j++)
				if (grid[i][j] == '?')
					grid[i][j] = grid[i][j-1];
		//right->left
		for (int i = 0; i < r; i++)
			for (int j = c-2; j >= 0; j--)
				if (grid[i][j] == '?')
					grid[i][j] = grid[i][j+1];
		//down->up
		for (int i = 1; i < r; i++)
			for (int j = 0; j < c; j++)
				if (grid[i][j] == '?')
					grid[i][j] = grid[i-1][j];
		//up->down
		for (int i = r-2; i >= 0; i--)
			for (int j = 0; j < c; j++)
				if (grid[i][j] == '?')
					grid[i][j] = grid[i+1][j];

		printf ("Case #%d:\n", k);
		for (int i = 0; i < r; i++)
			printf ("%s\n", grid[i]);
	}

	return 0;
}
