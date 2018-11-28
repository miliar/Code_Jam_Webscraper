// 2a-cake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>
using namespace std;

void runCase()
{
	// input
	int numRows = 0;
	int numColumns = 0;

	cin >> numRows >> numColumns;

	vector<string> rows;

	for (int i = 0; i < numRows; i++)
	{
		string row = "";
		cin >> row;

		for (int j = 0; j < numColumns; j++)
		{
			// look forward
			if (row[j] == '?')
			{
				for (int k = j + 1; k < numColumns; k++)
				{
					if (row[k] != '?')
					{
						row[j] = row[k];
						break;
					}
				}
			}

			// look back
			if (row[j] == '?')
			{
				for (int k = j - 1; k >= 0; k--)
				{
					if (row[k] != '?')
					{
						row[j] = row[k];
						break;
					}
				}
			}
		}

		rows.push_back(row);
	}

	for (int j = 0; j < numColumns; j++)
	{
		// look down
		for (int i = 0; i < numRows; i++)
		{
			if (rows.at(i)[j] == '?')
			{
				for (int k = i + 1; k < numRows; k++)
				{
					if (rows.at(k)[j] != '?')
					{
						rows.at(i)[j] = rows.at(k)[j];
						break;
					}
				}
			}

			if (rows.at(i)[j] == '?')
			{
				for (int k = i - 1; k >= 0; k--)
				{
					if (rows.at(k)[j] != '?')
					{
						rows.at(i)[j] = rows.at(k)[j];
						break;
					}
				}
			}
		}
	}

	// output
	for (int i = 0; i < numRows; i++)
	{
		cout << rows.at(i) << endl;
	}
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		cout << "Case #" << i + 1 << ":" << endl;
		runCase();
	}
}

