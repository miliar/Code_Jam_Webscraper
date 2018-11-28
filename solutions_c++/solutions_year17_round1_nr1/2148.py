#if 1
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

FILE* pF;

FILE* pAnsF;

int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);

	freopen_s(&pAnsF, "1output.txt", "w", stdout);
	
	int Cases;
	
	cin >> Cases;
	int R, C;
	char arr[27][27];
	for (int c = 1; c <= Cases; c++)
	{		
		cin >> R >> C;

		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cin >> arr[i][j];
			}
		}
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (arr[i][j] != '?')
				{
					for (int k = j + 1; k < C; k++)
					{
						if (arr[i][k] == '?')
							arr[i][k] = arr[i][j];
						else
							break;
					}
					for (int k = j - 1; k >= 0; k--)
					{
						if (arr[i][k] == '?')
							arr[i][k] = arr[i][j];
						else
							break;
					}
				}
			}
		}
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				int span = 0;
				if (arr[i][j] != '?')
				{
					for (int k = j ; k < C; k++)
					{
						if (arr[i][k] != arr[i][j])
							break;
						else
							span++;
					}
					for (int l = i+1;l<R; l++)
					{
						bool place = true;
						for (int m = j; m < j + span; m++)
						{
							if (arr[l][m] != '?')
								place = false;
						}
						if (place)
						{
							for (int m = j; m < j + span; m++)
								arr[l][m] = arr[i][j];
						}
						else
							break;
					}
					for (int l = i - 1; l>=0; l--)
					{
						bool place = true;
						for (int m = j; m < j + span; m++)
						{
							if (arr[l][m] != '?')
								place = false;
						}
						if (place)
						{
							for (int m = j; m < j + span; m++)
								arr[l][m] = arr[i][j];
						}
						else
							break;
					}

				}
			}
		}
		cout << "Case #" << c << ": " <<  endl;		
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cout << arr[i][j];
			}
			cout << endl;
		}
	}

	return 0;
}
#endif