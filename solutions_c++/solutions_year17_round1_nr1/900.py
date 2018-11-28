#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string.h>
#include <queue>
#include <list>
#include <iomanip>
#include <string>

using namespace std;

#define ll long long

ll MODE = 1000000007;

ll R, C;

vector<string> matrix;

void SingleProcess(ofstream& fout)
{

	for (int row = 0; row < R; row++)
	{
		for (int col = 1; col < C; col++)
		{
			if (matrix[row][col] == '?')
			{
				matrix[row][col] = matrix[row][col - 1];
			}
		}
	}


	for (int row = 0; row < R; row++)
	{
		for (int col = C-2; col >=0; col--)
		{
			if (matrix[row][col] == '?')
			{
				matrix[row][col] = matrix[row][col + 1];
			}
		}
	}

	for (int row = 1; row < R; row++)
	{
		if (matrix[row][0] == '?')
		{
			for (int col = 0; col < C; col++)
			{
				matrix[row][col] = matrix[row - 1][col];
			}
		}
	}

	for (int row = R-2; row >=0;row--)
	{
		if (matrix[row][0] == '?')
		{
			for (int col = 0; col < C; col++)
			{
				matrix[row][col] = matrix[row + 1][col];
			}
		}
	}

	for (int row = 0; row < R; row++)
	{
		for (int col = 0; col < C; col++)
		{
			fout << matrix[row][col];
		}
		fout << endl;
	}

}


int main()
{
	FILE* fp = freopen("in.txt", "r", stdin);
	ofstream fout("out.txt");
	int Cases = 0;
	scanf("%d", &Cases);
	for (int time = 0; time < Cases; time++)
	{
		cin >> R >> C;
		matrix.clear();
		for (int i = 0; i < R; i++)
		{
			matrix.push_back("");
		}
		char ch[100];
		for (int i = 0; i < R; i++)
		{
			cin >> ch;
			matrix[i] = ch;
		}

		fout << "Case #" << (time + 1) << ":"<<endl;
		SingleProcess(fout);
		//fout << endl;
		std::cout << time << endl;
	}
	fclose(fp);
	fout.close();

	return 0;

}