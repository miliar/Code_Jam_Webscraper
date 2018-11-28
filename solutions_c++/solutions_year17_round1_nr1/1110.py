#include <bits/stdc++.h>

using namespace std;

char mat[30][30];
int r, c;

void fill(int i, int j)
{
	char c = mat[i][j];
	for (int k = j+1; k < c and mat[i][k] == '?'; ++k)
		mat[i][k] = c;
	for (int k = j-1; k >= 0 and mat[i][k] == '?'; --k)
		mat[i][k] = c;
}

int main()
{
	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--) {
		scanf("%d %d", &r, &c);

		for (int i = 0; i < r; ++i)
			scanf("%s", mat[i]);

		int first = r, last = 0;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (mat[i][j] != '?')
				{
					first = min(first, i);
					last = max(last, i);
					fill(i, j);
				}

		for (int i = first-1; i >= 0; --i)
			for (int j = 0; j < c; ++j)
				mat[i][j] = mat[i+1][j];

		for (int i = last+1; i < r; ++i)
			for (int j = 0; j < c; ++j)
				mat[i][j] = mat[i-1][j];

		for (int i = 1; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (mat[i][j] == '?')
					mat[i][j] = mat[i-1][j];

		printf("Case #%d:\n", caso++);
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
				printf("%c", mat[i][j]);
			printf("\n");
		}
	}
	
	return 0;
}