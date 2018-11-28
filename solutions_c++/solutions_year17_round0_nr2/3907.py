#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<cmath>

using namespace std;

int t;
int ans;
int check(int x)
{
	int ps = 9;
	while (x)
	{
		if (ps < x % 10)
		{
			return 0;
		}
		ps = x % 10;
		x /= 10;
	}
	return 1;
}

int main()
{
	freopen("B-small-attempt0 (1).in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> ans;
		cout << "Case #" << i + 1 << ": ";
		while (ans)
		{
			if (check(ans))
			{
				cout << ans << "\n";
				break;
			}
			ans--;
		}
	}
	return 0;
}