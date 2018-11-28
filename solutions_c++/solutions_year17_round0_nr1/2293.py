#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:160777216")
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <stack>
#include <queue>
#define PI acos(-1.0)
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define INF 10000
#define eps 1e-12
#define ll long long
#define f0(i , n) for (int i = 0; i < n; i++)
#define NMAX 5000

using namespace std;

int test, i, j, k , t;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> test;
	for (t = 1; t <= test; t++)
	{
		string s;
		cin >> s >> k;
		int ans = 0;
		for (i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				if (i + k - 1 >= s.size())
				{
					ans = s.size();
					break;
				}

				ans++;
				for (j = i; j < i + k; j++)
				{
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}

		cout << "Case #" << t << ": ";
		if (ans >= s.size())
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;
	}
	return 0;
}