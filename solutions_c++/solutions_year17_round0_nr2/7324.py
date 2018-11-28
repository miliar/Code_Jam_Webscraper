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

void setNine(string & str, int pos)
{
	for (int i = pos; i < str.size(); ++i)
	{
		str[i] = '9';
	}
}

int confl(string & str)
{
	for (int i = 0; i < str.size() - 1; ++i)
	{
		if (str[i] > str[i + 1])
		{
			str[i]--;
			return i + 1;
		}
	}
	return -1;
}

int main() {
#ifdef _CONSOLE
	freopen("B-large (2).in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		string str;
		cin >> str;
		int tmp = confl(str);
		while (tmp != -1)
		{
			setNine(str, tmp);
			tmp = confl(str);
		}
		if (str[0] == '0' && str.size() > 1)
		{
			str = str.substr(1);
		}

		printf("Case #%d: %s\n", t, str.c_str());

	}


	return 0;
}