#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>
#include <cmath>
#include <stack>
#define int long long
#define CONTAINS(v,n) (find((v).begin(), (v).end(), (n)) != (v).end())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define ARY_SORT(a, size) sort((a), (a)+(size))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;


signed main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int H, W;
		cin >> H >> W;
		bool chars[26] = { 0 };
		char cell[25][25];
		for (int y = 0; y < H; y++)
		{
			string str;
			cin >> str;
			for (int x = 0; x < W; x++)
			{
				char ch = str[x];
				cell[x][y] = ch;
				if (ch != '?')
				{
					chars[ch - 'A'] = true;
				}
			}
		}

		int left[26];
		int right[26];
		int cy[26];

		for (int i = 0; i < 26; i++)
		{
			if (chars[i])
			{
				char ch = i + 'A';
				for (int x = 0; x < W; x++)
				{
					for (int y = 0; y < H; y++)
					{
						if (cell[x][y] == ch)
						{
							left[i] = x;
							right[i] = x;
							cy[i] = y;
						}
					}
				}
				//Å©
				for (int x = left[i] - 1; x >= 0; x--)
				{
					if (cell[x][cy[i]] == '?')
					{
						cell[x][cy[i]] = ch;
						left[i] = x;
					}
					else
					{
						break;
					}
				}
				//Å®
				for (int x = right[i] + 1; x < W; x++)
				{
					if (cell[x][cy[i]] == '?')
					{
						cell[x][cy[i]] = ch;
						right[i] = x;
					}
					else
					{
						break;
					}
				}
			}
		}
		for (int i = 0; i < 26; i++)
		{
			if (chars[i])
			{
				char ch = i + 'A';
				//Å™
				for (int y = cy[i] - 1; y >= 0; y--)
				{
					bool ok = true;
					for (int x = left[i]; x <= right[i]; x++)
					{
						if (cell[x][y] != '?')
						{
							ok = false;
							break;
						}
					}
					if (ok)
					{
						for (int x = left[i]; x <= right[i]; x++)
						{
							cell[x][y] = ch;
						}
					}
					else
					{
						break;
					}
				}
				//Å´
				for (int y = cy[i] + 1; y < H; y++)
				{
					bool ok = true;
					for (int x = left[i]; x <= right[i]; x++)
					{
						if (cell[x][y] != '?')
						{
							ok = false;
							break;
						}
					}
					if (ok)
					{
						for (int x = left[i]; x <= right[i]; x++)
						{
							cell[x][y] = ch;
						}
					}
					else
					{
						break;
					}
				}
			}
		}

		cout << "Case #" << (t + 1) << ":" << endl;
		for (int y = 0; y < H; y++)
		{
			for (int x = 0; x < W; x++)
			{
				cout << cell[x][y];
			}
			cout << endl;
		}
	}
}
