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

int t, k;
string s;

int main()
{
	freopen("A-large.in", "r", stdin); 
	//freopen("input.txt", "r", stdin); 
	freopen("output.txt", "w", stdout);
	cin >> t;

	int flag = 0;
	int cnt = 0;
	int a = 0;
	int l = 0;
	for (int j = 0; j < t; ++j)
	{
		cin >> s >> k;
		printf("Case #%d: ", j + 1);
		int n = (int)s.size();
		ll res = 0;

		string s1 = s;
		string s2 = s;
		bool check = 1;

		while (check)
		{
			check = 0;
			s2 = s1;
			for (int i = 0; i < n; ++i)
			{
				if (s1[i] == '-')
				{
					res++;
					if (i + k < n)
					{
						for (int j = i; j < i + k; ++j)
						{
							if (s1[j] == '-')
								s1[j] = '+';
							else
							{
								s1[j] = '-';
								check = 1;
							}
						}
					}
					else
					{
						for (int j = n - 1; j > n - 1 - k; --j)
						{
							if (s1[j] == '-')
								s1[j] = '+';
							else
							{
								s1[j] = '-';
								check = 1;
							}
						}
					}
				}
			}
			if ((s1 == s || s1 == s2) && check != 0)
			{

				check = 0;
				if (res != 0)
					res = -1;
			}
		}
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}

	return 0;
}