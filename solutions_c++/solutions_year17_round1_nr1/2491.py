#include<stdio.h>

FILE* INP;
FILE* OUP;

void test(int num);

void DC(int x, int y, int R, int C);

char map[30][30] = { 0 };

int main()
{
	INP = fopen("C:\\inpoup\\inp.txt", "rt");
	OUP = fopen("C:\\inpoup\\oup.txt", "wt");
	int n;
	fscanf(INP, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		test(i);
		printf("Case#%d done\n", i + 1);
	}
	return 0;
}

void test(int num)
{
	fprintf(OUP, "Case #%d: \n", num + 1);
	int R, C;
	fscanf(INP, "%d%d", &R, &C);
	int i, j;
	fscanf(INP,"\n");
	for (i = 0; i < R; i++)
	{
		for (j = 0; j < C; j++)	fscanf(INP, "%c", &map[i][j]);
		fscanf(INP, "\n");
	}

	DC(0, 0, R, C);
	for (i = 0; i < R; i++)
	{
		for (j = 0; j < C; j++)
		{
			fprintf(OUP, "%c", map[i][j]);
		}
		fprintf(OUP, "\n");
	}
}

void DC(int x, int y, int R, int C)
{
	int i, j;
	char last = '?';
	int lastx, lasty;
	for (i = x; i < x + R; i++)
	{
		for (j = y; j < y + C; j++)
		{
			if (map[i][j] != '?')
			{
				if (last != map[i][j] && last != '?')
				{
					if (lastx != i)
					{
						DC(x, y, i - x, C);
						DC(i, y, R - i + x, C);
						return;
					}
					else if (lasty != j)
					{
						DC(x, y, R, j - y);
						DC(x, j, R, C - j + y);
						return;
					}
				}
				last = map[i][j];
				lastx = i;
				lasty = j;
			}
		}
	}
	for (i = x; i < x + R; i++) for (j = y; j < y + C; j++) map[i][j] = last;
	return;
}