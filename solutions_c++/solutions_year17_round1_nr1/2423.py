#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <ctime>

// #include <cstdio>
//#include <sstream>

using namespace std;

#define TASK "task1"

int main()
{
//	clock_t begin = clock();

	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	ios_base::sync_with_stdio(false);

	int t; // kolvo_testovih_zadac;
	int r, c;
	int res;
	string row;
	string temp_row;
	vector<string> field;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> r;
		cin >> c;
		field.clear();
		for (int j = 0; j < r; j++)
		{
			row.clear();
			row.resize(c);
			cin >> row;
			field.push_back(row);
		}
		for (int j = 0; j < r; j++)
		{
			row.clear();
			temp_row.clear();
			row = field[j];
			temp_row = row;
			sort(temp_row.begin(), temp_row.end());
			for (int q = 0; q < temp_row.size(); q++)
			{
				if (temp_row[q] != '?')
				{
					auto it1 = std::find(row.begin(), row.end(), temp_row[q]);
					auto it2 = std::find(row.begin(), row.end(), temp_row[q]);
					it1++;
					while (*it1 == '?')
					{
						*it1 = temp_row[q];
						it1++;
					}
					it2--;
					while (*it2 == '?')
					{
						*it2 = temp_row[q];
						it2--;
					}
				}
			}
			field[j] = row;

		}
		for (int j = 0; j < r; j++)
		{
			if ((field[j][0] == '?')&&(j > 0))
			{
				field[j] = field[j - 1];
		    }
		}
		for (int j = r-1; j > -1; j--)
		{
			if ((field[j][0] == '?') && (j < r-1))
			{
				field[j] = field[j + 1];
			}
		}
		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < r; j++)
		{
			cout << field[j] << endl;
		}
	}

//	clock_t end = clock();
//	long elapsed_secs = end - begin;
//	cout << "time" << elapsed_secs; 

}