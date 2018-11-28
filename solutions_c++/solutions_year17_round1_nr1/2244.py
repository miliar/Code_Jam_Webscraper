
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cstring>
#include <iomanip>

using namespace std;

ifstream in("fracdec.in");
ofstream out("fracdec.out");

char zGrid[50][50];
int R, C;

char FindFirstChar(int iRow)
{

	for (int k = 0; k < C; ++k)
	{
		if (zGrid[iRow][k] != '?')
			return zGrid[iRow][k];
	}
	
	return '?';
}

int FindRow(int iRow)
{
	for (int k = iRow - 1; k >= 0; --k)
	{
		if (zGrid[k][0] != '?')
			return k;
	}

	for (int k = iRow + 1; k < R; ++k)
	{
		if (zGrid[k][0] != '?')
			return k;
	}

	return -1;
}

int main()
{
	int T;
	in >> T;

	for (int i = 1; i <= T; ++i)
	{
		
		in >> R >> C;

		for (int j = 0; j < R; ++j)
		{
			for (int k = 0; k < C; ++k)
			{
				in >> zGrid[j][k];
			}
		}

		for (int j = 0; j < R; ++j)
		{
			char cFirstChar = FindFirstChar(j);

			if (cFirstChar == '?')
				continue;

			for (int k = 0; k < C; ++k)
			{
				if (zGrid[j][k] == '?')
				{
					zGrid[j][k] = cFirstChar;
				}
				else if (zGrid[j][k] != cFirstChar)
				{
					cFirstChar = zGrid[j][k];
				}
			}
		}

		for (int j = 0; j < R; ++j)
		{
			char cFirstChar = FindFirstChar(j);

			if (cFirstChar != '?')
				continue;

			int iRow = FindRow(j);

			for (int k = 0; k < C; ++k)
			{
				zGrid[j][k] = zGrid[iRow][k];
			}
		}

		out << "Case #" << i << ":" << endl;

		for (int j = 0; j < R; ++j)
		{
			for (int k = 0; k < C; ++k)
			{
				out << zGrid[j][k];

				if (zGrid[j][k] < 'A' || zGrid[j][k] > 'Z')
					cout << (int)zGrid[j][k] << endl;
			}
			out << endl;
		}
	}

	return 0;
}

