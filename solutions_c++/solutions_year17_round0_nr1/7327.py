#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;

void change(string & str, int pos, int k)
{
	for (int i = 0; i < k; ++i)
	{
		if (str[pos + i] == '+')
			str[pos + i] = '-';
		else
			str[pos + i] = '+';
	}
}

bool check(string& str)
{
	for (int i = 0; i < str.size(); ++i)
	{
		if (str[i] == '-')
			return false;
	}
}

int main() {
#ifdef _CONSOLE
	freopen("A-large (2).in", "r", stdin);
	freopen("out2.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		string str;
		int k;
		cin >> str >> k;
		int ans = 0;
		for (int i = 0; i <= (int)str.size() - k; ++i)
		{
			if (str[i] == '-')
			{
				change(str, i, k);
				ans++;
			}
		}

		if (check(str))
		{
			printf("Case #%d: %d\n", t, ans);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}

	}


	return 0;
}