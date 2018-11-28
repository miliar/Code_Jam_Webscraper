// 3rd party library - CPLEX is used for solving the integer programming

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int N, P;
int G[105];
int Rem[4];
int DP[105][105][105];

void PreDP()
{
	for (int i1 = 0; i1 <= 100; i1 ++)
		for (int i2 = 0; i2 <= 100; i2 ++)
			for (int i3 = 0; i3 <= 100; i3 ++)
			{
				if (i1 >= 4 && i2 >= 0 && i3 >= 0) DP[i1][i2][i3] = max(DP[i1][i2][i3], DP[i1 - 4][i2 - 0][i3 - 0] + 1);
				if (i1 >= 0 && i2 >= 0 && i3 >= 4) DP[i1][i2][i3] = max(DP[i1][i2][i3], DP[i1 - 0][i2 - 0][i3 - 4] + 1);
				if (i1 >= 0 && i2 >= 2 && i3 >= 0) DP[i1][i2][i3] = max(DP[i1][i2][i3], DP[i1 - 0][i2 - 2][i3 - 0] + 1);
				if (i1 >= 2 && i2 >= 1 && i3 >= 0) DP[i1][i2][i3] = max(DP[i1][i2][i3], DP[i1 - 2][i2 - 1][i3 - 0] + 1);
				if (i1 >= 0 && i2 >= 1 && i3 >= 2) DP[i1][i2][i3] = max(DP[i1][i2][i3], DP[i1 - 0][i2 - 1][i3 - 2] + 1);
				if (i1 >= 1 && i2 >= 0 && i3 >= 1) DP[i1][i2][i3] = max(DP[i1][i2][i3], DP[i1 - 1][i2 - 0][i3 - 1] + 1);
			}
}

void Work()
{
	scanf("%d%d", &N, &P);
	memset(Rem, 0, sizeof(Rem));
	for (int i = 0; i < N; i ++)
	{
		scanf("%d", &G[i]);
		Rem[G[i] % P] ++;
	}
	int Ans = Rem[0], Ans2 = Rem[0];
	if (P == 2)
	{
		Ans += (Rem[1] + 1) / 2;
	}
	else if (P == 3)
	{
		// 12
		int min12 = min(Rem[1], Rem[2]);
		Ans += min12;
		Rem[1] -= min12;
		Rem[2] -= min12;
		// 111
		int min111 = Rem[1] / 3;
		Ans += min111;
		Rem[1] -= min111 * 3;
		// 222
		int min222 = Rem[2] / 3;
		Ans += min222;
		Rem[2] -= min222 * 3;
		if (Rem[1] || Rem[2])
			Ans ++;
	}
	else
	{
		int tmp = 0;
		for (int i1 = 0; i1 <= Rem[1]; i1 ++)
			for (int i2 = 0; i2 <= Rem[2]; i2 ++)
				for (int i3 = 0; i3 <= Rem[3]; i3 ++)
					tmp = max(tmp, DP[i1][i2][i3] + (i1 != Rem[1] || i2 != Rem[2] || i3 != Rem[3]));
		Ans2 += tmp;

		
		// 22
		int min22 = Rem[2] / 2;
		Ans += min22;
		Rem[2] -= min22 * 2;
		// 13
		int min13 = min(Rem[1], Rem[3]);
		Ans += min13;
		Rem[1] -= min13;
		Rem[3] -= min13;
		if (Rem[2])
		{
			if (Rem[1] >= 2)
			{
				// 211
				Rem[1] -= 2;
				Rem[2] -= 1;
				Ans ++;
			}
			else if (Rem[3] >= 2)
			{
				// 233
				Rem[3] -= 2;
				Rem[2] -= 1;
				Ans ++;
			}
			// else no useful
		}
		// maybe Rem[2] left
		// 1111
		int min1111 = Rem[1] / 4;
		Ans += min1111;
		Rem[1] -= min1111 * 4;
		// 3333
		int min3333 = Rem[3] / 4;
		Ans += min3333;
		Rem[3] -= min3333 * 4;
		if (Rem[1] || Rem[2] || Rem[3])
			Ans ++;
	}
	printf("%d\n", Ans);
	/*if (P == 4)
	{
		printf("%d\n", Ans2);
		if (Ans != Ans2)
			printf("ERROR\n");
	}*/
}

int main()
{
	PreDP();
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		fprintf(stderr, "Case #%d: \n", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}
