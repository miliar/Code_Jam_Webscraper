#include<stdio.h>

int T;
int D2[101][101][2];
int D3[101][101][101][3];
int D4[101][101][101][101][4];
int M2[10], M3[10], M4[10];
int N, P, G;

int main(void)
{
	int c0, c1, c2, c3, curr, plus;
	int l0, l1;

	for(l1 = 0; l1 < 10; l1++)
	{
		M2[l1] = l1 % 2;
		M3[l1] = l1 % 3;
		M4[l1] = l1 % 4;
	}

	for(c0 = 0; c0 <= 100; c0++)
	{
		for(c1 = 0; c1 <= 100; c1++)
		{
			for(curr = 0; curr <= 1; curr++)
			{
				plus = (curr == 0);
				if(c0 > 0)
				{
					if(D2[c0][c1][curr] < D2[c0-1][c1][curr] + plus)
					{
						D2[c0][c1][curr] = D2[c0-1][c1][curr] + plus;
					}
				}
				if(c1 > 0)
				{
					if(D2[c0][c1][curr] < D2[c0][c1-1][M2[curr+1]] + plus)
					{
						D2[c0][c1][curr] = D2[c0][c1-1][M2[curr+1]] + plus;
					}
				}
			}
		}
	}

	for(c0 = 0; c0 <= 100; c0++)
	{
		for(c1 = 0; c1 <= 100; c1++)
		{
			for(c2 = 0; c2 <= 100; c2++)
			{
				for(curr = 0; curr <= 2; curr++)
				{
					plus = (curr == 0);
					if(c0 > 0)
					{
						if(D3[c0][c1][c2][curr] < D3[c0-1][c1][c2][curr] + plus)
						{
							D3[c0][c1][c2][curr] = D3[c0-1][c1][c2][curr] + plus;
						}
					}
					if(c1 > 0)
					{
						if(D3[c0][c1][c2][curr] < D3[c0][c1-1][c2][M3[curr+1]] + plus)
						{
							D3[c0][c1][c2][curr] = D3[c0][c1-1][c2][M3[curr+1]] + plus;
						}
					}
					if(c2 > 0)
					{
						if(D3[c0][c1][c2][curr] < D3[c0][c1][c2-1][M3[curr+2]] + plus)
						{
							D3[c0][c1][c2][curr] = D3[c0][c1][c2-1][M3[curr+2]] + plus;
						}
					}
				}
			}
		}
	}

	for(c0 = 0; c0 <= 100; c0++)
	{
		for(c1 = 0; c1 <= 100; c1++)
		{
			for(c2 = 0; c2 <= 100; c2++)
			{
				for(c3 = 0; c3 <= 100; c3++)
				{
					for(curr = 0; curr <= 1; curr++)
					{
						plus = (curr == 0);
						if(c0 > 0)
						{
							if(D4[c0][c1][c2][c3][curr] < D4[c0-1][c1][c2][c3][curr] + plus)
							{
								D4[c0][c1][c2][c3][curr] = D4[c0-1][c1][c2][c3][curr] + plus;
							}
						}
						if(c1 > 0)
						{
							if(D4[c0][c1][c2][c3][curr] < D4[c0][c1-1][c2][c3][M4[curr+1]] + plus)
							{
								D4[c0][c1][c2][c3][curr] = D4[c0][c1-1][c2][c3][M4[curr+1]] + plus;
							}
						}
						if(c2 > 0)
						{
							if(D4[c0][c1][c2][c3][curr] < D4[c0][c1][c2-1][c3][M4[curr+2]] + plus)
							{
								D4[c0][c1][c2][c3][curr] = D4[c0][c1][c2-1][c3][M4[curr+2]] + plus;
							}
						}
						if(c3 > 0)
						{
							if(D4[c0][c1][c2][c3][curr] < D4[c0][c1][c2][c3-1][M4[curr+3]] + plus)
							{
								D4[c0][c1][c2][c3][curr] = D4[c0][c1][c2][c3-1][M4[curr+3]] + plus;
							}
						}
					}
				}
			}
		}
	}

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &N, &P);
		c0 = c1 = c2 = c3 = 0;
		for(l1 = 0; l1 < N; l1++)
		{
			scanf("%d", &G);
			G %= P;
			if(G == 0) c0++;
			if(G == 1) c1++;
			if(G == 2) c2++;
			if(G == 3) c3++;
		}
		if(P == 2) printf("Case #%d: %d\n", l0, D2[c0][c1][0]);
		if(P == 3) printf("Case #%d: %d\n", l0, D3[c0][c1][c2][0]);
		if(P == 4) printf("Case #%d: %d\n", l0, D4[c0][c1][c2][c3][0]);
	}

	return 0;
}
