#include <bits/stdc++.h>
using namespace std;

#define ull unsigned long long
#define ll long long
#define l long
#define nl cout << endl;

/* DEBUGGER */
#define bug printf("Bug");
#define boom printf("Boom");

void print_case(int i)
{
	cout << "Case #" << i << ":";
}

int main()
{
	int R, C, T;
	int i, j;
	cin >> T;
	string a[30];
	for (int x = 1; x <= T; ++x)
	{
		cin >> R >> C;
		for (i = 0; i < R; ++i)
		{
			a[i].clear();
			cin >> a[i];
		}

		if (a[0][0] == '?')
		{
			if (a[i][1] != '?')
			{
				a[i][0] = a[i][1];
			}
			else if (a[i+1][0] != '?')
			{
				a[i][0] = a[i+1][0];
			}
		}
		int count;
		do
		{
			count = 0;
			for (i = 0; i < R; ++i)
			{
				for (j = 0; j < C; ++j)
				{
					if (a[i][j] == '?')
					{
						if (i < R-1 && a[i+1][j] != '?')
						{
							a[i][j] = a[i+1][j];
							++count;
						}
						else if (i > 0 && a[i-1][j] != '?')
						{
							a[i][j] = a[i-1][j];
							++count;
						}		
					}
				}
			}
		} while (count > 0);
		do
		{
			count = 0;
			for (i = 0; i < R; ++i)
			{
				for (j = 0; j < C; ++j)
				{
					if (a[i][j] == '?')
					{
						if (j > 0 && a[i][j-1] != '?')
						{
							a[i][j] = a[i][j-1];
							++count;
						}
						else if (j < C-1 && a[i][j+1] != '?')
						{
							a[i][j] = a[i][j+1];
							++count;
						}				
					}
				}
			}
		} while (count > 0);

		print_case(x); nl;
		for (i = 0; i < R; ++i)
		{
			cout << a[i] << endl;
		}
	}
	return 0;
}