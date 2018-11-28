#include <iostream>
#include <string>

using namespace std;

int currCase = 1;
int cases;

void print(const string &solution)
{
	cout << "Case #" << currCase << ": " << solution << '\n';
	++currCase;
}

void cake()
{
	int r, c;

	cin >> r >> c;

	char** cake;

	cake = new char*[r];
	for (int i = 0; i < r; ++i)
	{
		cake[i] = new char[c];
	}

	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			cin >> cake[i][j];
		}
	}

	for (int i = 0; i < r; ++i)
	{
		char initial = '?';

		for (int j = 0; j < c; ++j)
		{
			if (cake[i][j] != '?')
			{
				initial = cake[i][j];
			}
			cake[i][j] = initial;
		}
	}

	for (int i = 0; i < r; ++i)
	{
		char initial = '?';

		for (int j = c - 1; j >= 0; --j)
		{
			if (cake[i][j] != '?')
			{
				initial = cake[i][j];
			}
			cake[i][j] = initial;
		}
	}

	for (int i = 1; i < r; ++i)
	{
		char initial = '?';

		if (cake[i][0] == '?')
		{
			for (int j = 0; j < c; ++j)
			{
				cake[i][j] = cake[i - 1][j];
			}
		}
	}

	for (int i = r - 2; i > 0; --i)
	{
		char initial = '?';

		if (cake[i][0] == '?')
		{
			for (int j = 0; j < c; ++j)
			{
				cake[i][j] = cake[i + 1][j];
			}
		}
	}

	if (cake[0][0] == '?')
	{
		for (int j = 0; j < c; ++j)
		{
			cake[0][j] = cake[1][j];
		}
	}

	print("");
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			cout << cake[i][j];
		}
		cout << endl;
	}

	for (int i = 0; i < r; ++i)
	{
		delete[] cake[i];
	}
	delete[] cake;
}

int main()
{
	cin >> cases;

	for (int i = 0; i < cases; ++i)cake();
}