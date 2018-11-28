#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>

using namespace std;

typedef long long LL;

bool check(int x)
{
	string s = "";
	while (x)
	{
		s += (x % 10 + '0');
		x /= 10;
	}
	reverse(s.begin(), s.end());
	for (int i = 1; i < s.size(); i++)
	{
		if (s[i] < s[i - 1])
			return false;
	}
	return true;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	vector<int> tidys;
	for (int i = 1; i <= 1000; i++)
	{
		if (check(i))
			tidys.push_back(i);
	}
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		int el;
		cin >> el;

		cout << "Case #" << i << ": " << *(--upper_bound(tidys.begin(), tidys.end(), el)) << "\n";
	}
	return 0;
}