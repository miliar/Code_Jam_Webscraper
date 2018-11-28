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

char data[1005];
int n;
int t;

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int ans = 0;
		cin >> data >> n;
		cout << "Case #" << i + 1 << ": ";
		int len = strlen(data);
		for (int j = 0; j < len - n + 1; j++)
		{
			if (data[j] == '-')
			{
				ans++;
				for (int k = 0; k < n; k++)
				{
					if (data[j+k] == '+')
					{
						data[j+k] = '-';
					}
					else
					{
						data[j+k] = '+';
					}
				}
			}
		}
		int ok = 0;
		for (int j = 0; j < len; j++)
		{
			if (data[j] == '-')
			{
				ok = 1;
				break;
			}
		}
		if (ok)
		{
			cout << "IMPOSSIBLE\n";
		}
		else
		{
			cout << ans << "\n";
		}
	}
	return 0;
}