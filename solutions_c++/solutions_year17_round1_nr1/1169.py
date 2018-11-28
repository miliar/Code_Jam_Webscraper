#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

bool IsEmptyRow(const string& row)
{
	return std::none_of(row.begin(), row.end(), [](char c) {return c != '?'; });
}

void ChangeRow(string& row)
{
	int column = 0;
	while (row[column] == '?')
	{
		++column;

		if (column == row.size())
		{
			return;
		}
	}

	for (int i = 0; i < column; ++i)
	{
		row[i] = row[column];
	}

	for (int i = column + 1; i < (int)row.size(); ++i)
	{
		if (row[i] == '?')
		{
			row[i] = row[i - 1];
		}
	}
}

void Solve(vector<string>& originalCake)
{
	int rowCount = originalCake.size();
	int firstNoneEmptyRow = 0;
	while (IsEmptyRow(originalCake[firstNoneEmptyRow]))
	{
		++firstNoneEmptyRow;
	}

	ChangeRow(originalCake[firstNoneEmptyRow]);
	for (int i = 0; i < firstNoneEmptyRow; ++i)
	{
		originalCake[i] = originalCake[firstNoneEmptyRow];
	}

	for (int i = firstNoneEmptyRow + 1; i < rowCount; ++i)
	{
		if (IsEmptyRow(originalCake[i]))
		{
			originalCake[i] = originalCake[i - 1];
		}
		else
		{
			ChangeRow(originalCake[i]);
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int R, C;
		scanf("%d %d", &R, &C);
		
		vector<string> cake;
		
		char line[30];
		for (int j = 0; j < R; ++j)
		{
			scanf("%s", line);
			cake.push_back(line);
		}
		
		printf("Case #%d:\n", i);
		
		Solve(cake);
		for (const string& row : cake)
		{
			printf("%s\n", row.c_str());
		}
	}
	
	return 0;
}
