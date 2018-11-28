#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		int R, C;
		cin >> R >> C;
		char a[R][C];
		for (int j=0; j<R; j++)
		{
			for (int k=0; k<C; k++)
				cin >> a[j][k];
		}

		// Solve the problem
		for (int y=0; y<R; y++)
		{
			for (int x=1; x<C; x++)
			{
				if (a[y][x] == '?' && a[y][x-1] != '?')
				{
					a[y][x] = a[y][x-1];
				}
			}
			for (int x=C-2; x>=0; x--)
			{
				if (a[y][x] == '?' && a[y][x+1] != '?')
				{
					a[y][x] = a[y][x+1];
				}
			}
		}

		for (int x=0; x<C; x++)
		{
			for (int y=1; y<R; y++)
			{
				if (a[y][x] == '?' && a[y-1][x] != '?')
				{
					a[y][x] = a[y-1][x];
				}
			}
			for (int y=R-2; y>=0; y--)
			{
				if (a[y][x] == '?' && a[y+1][x] != '?')
				{
					a[y][x] = a[y+1][x];
				}
			}
		}



		// Print result
		cout << "Case #" << i+1 << ":" << endl;
		for (int j=0; j<R; j++)
		{
			for (int k=0; k<C; k++)
				cout << a[j][k];
			cout << endl;
		}

	}

	return 0;

}