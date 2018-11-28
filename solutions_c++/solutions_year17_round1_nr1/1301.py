#include <bits/stdc++.h>
using namespace std;
char cake[50][50];
int r, c, t;
int main()
{
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				scanf(" %c", &cake[i][j]);
			}
		}
		for (int i = 0; i < r; i++)
		{
			char first = '?';
			for (int j = 0; j < c; j++)
			{
				if (first == '?') first = cake[i][j];
			}
			if (first == '?') continue;
			for (int j = 0; j < c; j++)
			{
				if (cake[i][j] == '?' || cake[i][j] == first)
				{
					cake[i][j] = first;
				}
				else first = cake[i][j];
			}
		}
	
	char last = 0;
	for (int i = 0; i < r; i++)
	{
		if (cake[i][0] != '?') last = i;
	}
	for (int i = 0; i < c; i++)
	{
		cake[r-1][i] = cake[last][i];
	}
	for (int i = r-1; i >= 0; i--)
	{
		if (cake[i][0] == '?')
		{
			for (int j = 0; j < c; j++)
			{
				cake[i][j] = cake[i+1][j];
			}
		}
	}
	printf("Case #%d:\n", i);
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++) printf("%c", cake[i][j]);
		printf("\n");
	}
}
}