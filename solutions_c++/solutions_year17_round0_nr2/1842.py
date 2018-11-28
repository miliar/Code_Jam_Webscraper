#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solve()
{
	long long n;
	cin >> n;
	vector <int> v;
	while (n > 0)
	{
		v.push_back(n % 10);
		n /= 10;
	}
	reverse(v.begin(), v.end());
	for (int i = 0; i + 1 < v.size(); ++i)
	{
		if (v[i] > v[i + 1])
		{
			int new_digit = v[i] == 1 ? 9 : v[i] - 1;
			int old_digit = v[i];
			for (int j = i; j >= 0 && v[j] == old_digit; --j)
			{
				v[j] = new_digit;
				if (j != i)
				{
					v[j + 1] = 9;
				}
			}
			for (int j = i + 1; j < v.size(); ++j)
			{
				v[j] = 9;
			}
			if (new_digit == 9)
			{
				v[0] = 0;
			}
			break;
		}
	}
	long long res = 0;
	for (int i = 0; i < v.size(); ++i)
	{
		res = res * 10 + v[i];
	}
	return res;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		long long ans = solve();
		cout << ans << endl;
	}
	return 0;
}
