#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
#include <iterator>
#include <complex>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MEM(x, y) memset((x),(y),sizeof(x))
const LL INF = 1e9 + 7;
const int N = 2e5 + 1;
string check(string str, int cur)
{
	if (str[cur] <= str[cur - 1]) return "";
	str[cur]--;
	for (int i = cur + 1; i < str.length(); i++) str[i] = '9';
	return str;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		string str;
		cin >> str;
		str = "0" + str;
		string ans = str;
		for (int i = 1; i < str.length(); i++)
		{
			if (str[i] < str[i - 1])
			{
				ans = "";
				break;
			}
		}
		for (int i = 1; i < str.length(); i++)
		{
			if (str[i] < str[i - 1]) break;
			if (str[i] == '0') continue;
			ans = max(ans, check(str, i));
		}
		while (ans[0] == '0') ans = ans.substr(1);
		printf("Case #%d: %s\n", ks++, ans.c_str());
	}
	return 0;
}

