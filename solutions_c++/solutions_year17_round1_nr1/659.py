#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <iostream>
using namespace std;

void solve(int tn)
{
	char matr[30][30];
	bool allQ[30];
	int r, c;
	cin >> r >> c;
	for (int i = 0; i < r; i++)
	{
		cin >> matr[i];
		allQ[i] = true;
		int startQ = 0;
		for (int j = 0; j < c; j++)
		{
			if (matr[i][j] != '?')
			{
				for (int k = startQ; k < j; k++)
					matr[i][k] = matr[i][j];
				startQ = j + 1;
			}
		}
		if (startQ != 0)
		{
			allQ[i] = false;
			for (int k = startQ; k < c; k++)
				matr[i][k] = matr[i][startQ - 1];
		}
	}

	int start = 0;
	for (int i = 0; i < r; i++)
	{
		if (!allQ[i])
		{
			for (int k = start; k < i; k++)
				strcpy(matr[k], matr[i]);
			start = i + 1;
		}
	}
	if (start != 0)
	{
		for (int k = start; k < r; k++)
			strcpy(matr[k], matr[start - 1]);
	}

	cout << "Case #" << tn << ":" << endl;
	for (int i = 0; i < r; i++)
		cout << matr[i] << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf_s("%d", &t);
	for (int it = 0; it < t; it++)
		solve(it + 1);
	return 0;
}
