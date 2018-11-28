#include <stdio.h>

int r, c;
const int maxr = 30;
const int maxc = 30;
const int maxchar = 30;

char data[maxr][maxc];
char usedchar[maxchar];
int charsize[maxchar][4];
int filldepth[maxr][maxc];

int min(int a, int b)
{
	if (a <= b) return a;
	return b;
}

int max(int a, int b)
{
	if (a >= b) return a;
	return b;
}

void init()
{
	int i, j, ind;

	for(i = 0; i < r; i++)
		for (j = 0; j < c; j++)
		{
			if (data[i][j] == '?')
				data[i][j] = -1;
			else data[i][j] -= 'A';
			filldepth[i][j] = -1;
		}
	for (i = 0; i < maxchar; i++)
		usedchar[i] = 0;
	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++)
		{
			if (data[i][j] != -1)
			{
				ind = data[i][j];
				if (usedchar[ind] == 0)
				{
					usedchar[ind] = 1;
					charsize[ind][0] = charsize[ind][1] = i;
					charsize[ind][2] = charsize[ind][3] = j;
				}
				else
				{
					charsize[ind][0] = min(charsize[ind][0], i);
					charsize[ind][1] = max(charsize[ind][1], i);
					charsize[ind][2] = min(charsize[ind][2], j);
					charsize[ind][3] = max(charsize[ind][3], j);
				}
			}
		}
}

int fill(int p, int q, int ind, int depth)
{
	int newsq[4], i, j;

	newsq[0] = min(charsize[ind][0], p);
	newsq[1] = max(charsize[ind][1], p);
	newsq[2] = min(charsize[ind][2], q);
	newsq[3] = max(charsize[ind][3], q);

	for (i = newsq[0]; i <= newsq[1]; i++)
	{
		for (j = newsq[2]; j <= newsq[3]; j++)
		{
			if (data[i][j] != -1 && data[i][j] != ind)
				return 0;
		}
	}

	for(i = newsq[0]; i <= newsq[1]; i++)
		for (j = newsq[2]; j <= newsq[3]; j++)
		{
			if (data[i][j] == -1)
			{
				data[i][j] = ind;
				filldepth[i][j] = depth;
			}
		}
	for (i = 0; i < 4; i++)
		charsize[ind][i] = newsq[i];
	return 1;
}

void fill_rev(int depth)
{
	int i, j;

	for(i = 0; i < r; i++)
		for (j = 0; j < c; j++)
		{
			if (filldepth[i][j] == depth)
			{
				filldepth[i][j] = -1;
				data[i][j] = -1;
			}
		}
}

int fill_in(int p, int depth)
{
	int i, j, k, t, l;
	int temp[4];

	for (i = p; i < r; i++)
	{
		for (j = 0; j < c; j++)
		{
			if (data[i][j] == -1)
			{
				for (k = 0; k < maxchar; k++)
				{
					if (usedchar[k])
					{
						temp[0] = charsize[k][0];
						temp[1] = charsize[k][1];
						temp[2] = charsize[k][2];
						temp[3] = charsize[k][3];
						if (fill(i, j, k, depth))
						{
							t = fill_in(p, depth + 1);
							if (t) return 1;
							fill_rev(depth);
							for (l = 0; l < 4; l++)
								charsize[k][l] = temp[l];
						}
					}
				}
			}
		}
	}
	return 1;
}

void process()
{
	init();
	fill_in(0, 0);
}

int main()
{
	int t, casenum, i, j;

	scanf("%d", &t);
	for (casenum = 1; casenum <= t; casenum++)
	{
		scanf("%d %d", &r, &c);
		for (i = 0; i < r; i++)
			scanf("%s", data[i]);
		process();
		printf("Case #%d:\n", casenum);
		for (i = 0; i < r; i++)
		{
			for (j = 0; j < c; j++)
				printf("%c", data[i][j] +'A');
			printf("\n");
		}
	}
	return 0;
}