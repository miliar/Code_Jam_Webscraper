#pragma comment(linker, "/STACK:256000000")
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include <set>
#include <queue>
#include <map>
#include <vector>

using namespace std;

#define mp make_pair
#define con continue
typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector < vector < int> > vvi;
typedef vector < vector < pair < int, int > > > vvii;

int t;
string s;
vector <char> ans;

int main()
{
	freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin); 
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int j = 0; j < t; ++j)
	{
		cin >> s;
		printf("Case #%d: ", j + 1);
		int n = (int)s.size();
		ans.clear();

		int pos = -1;
		char pr = '0';
		for (int i = 0; i < n; ++i)
		{
			if (s[i] >= pr)
			{
				pr = s[i];
				con;
			}
			else
			{
				pos = i;
				break;
			}
		}

		if (pos == -1)
		{
			cout << s << endl;
			con;
		}

		char forv = '*';
		pos--;
		for (int i = n - 1; i >= 0; --i)
		{
			if (i > pos)
			{
				ans.push_back('9');
				con;
			}
			else if (i == pos)
			{
				int x = s[i] - '0';
				x--;

				if (x == -1)
				{
					x = 9;
					pos--;
				}
				else if (x == 0 && i == 0)
					con;
				if (i - 1 >= 0)
				{
					int y = s[i - 1] - '0';
					if (x < y)
					{
						x = 9;
						pos--;
					}
				}
				ans.push_back(x + '0');
			}
			else
			{
				ans.push_back(s[i]);
			}
		}

		for (int i = (int)ans.size() - 1; i >= 0; --i)
			printf("%c", ans[i]);
		printf("\n");
	}

	return 0;
}